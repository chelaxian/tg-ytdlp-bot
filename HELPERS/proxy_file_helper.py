"""
Helper module for working with proxy list from TXT/proxy.txt file
"""
import os
import re
import logging
from typing import List, Dict, Optional, Tuple

logger = logging.getLogger(__name__)

# Mapping of country names from proxy.txt to normalized country names
# This helps match countries even if they're written differently
COUNTRY_MAPPING = {
    # Standard names
    'germany': 'germany',
    'russia': 'russia',
    'russian federation': 'russia',
    'united states': 'united states',
    'turkey': 'turkey',
    'italy': 'italy',
    'india': 'india',
    'georgia': 'georgia',
    'belarus': 'belarus',
    'thailand': 'thailand',
    'netherlands': 'netherlands',
    'united kingdom': 'united kingdom',
    # Common variations and abbreviations
    'usa': 'united states',
    'us': 'united states',
    'u.s.': 'united states',
    'u.s.a.': 'united states',
    'uk': 'united kingdom',
    'great britain': 'united kingdom',
    'britain': 'united kingdom',
    'u.k.': 'united kingdom',
    'g.b.': 'united kingdom',
}

def parse_proxy_file(file_path: str = "TXT/proxy.txt") -> List[Dict]:
    """
    Parse proxy.txt file and extract proxy information with countries.
    
    Args:
        file_path: Path to proxy.txt file
        
    Returns:
        List of dictionaries with proxy info: [{
            'type': 'http' or 'socks5',
            'country': 'Germany',
            'ip': '1.2.3.4',
            'port': '8080',
            'user': 'username',
            'password': 'password',
            'proxy_url': 'http://username:password@1.2.3.4:8080'
        }, ...]
    """
    proxies = []
    
    if not os.path.exists(file_path):
        logger.debug(f"Proxy file {file_path} does not exist")
        return proxies
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        if not content:
            logger.debug(f"Proxy file {file_path} is empty")
            return proxies
        
        current_type = None
        lines = content.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            # Check for section headers
            if line.upper().startswith('HTTP'):
                current_type = 'http'
                continue
            elif line.upper().startswith('SOCKS5'):
                current_type = 'socks5'
                continue
            
            # Parse proxy line: 🇩🇪 Germany – 1.2.3.4:8080:username:password
            # Format: [flag] Country – IP:PORT:USER:PASSWORD
            match = re.match(r'[^\w]*([A-Za-z\s]+?)\s*[–-]\s*(\d+\.\d+\.\d+\.\d+):(\d+):([^:]+):(.+)', line)
            if match:
                country = match.group(1).strip()
                ip = match.group(2)
                port = match.group(3)
                user = match.group(4)
                password = match.group(5)
                
                # Build proxy URL based on type
                if current_type == 'socks5':
                    proxy_url = f"socks5://{user}:{password}@{ip}:{port}"
                else:  # http or https
                    proxy_url = f"http://{user}:{password}@{ip}:{port}"
                
                proxies.append({
                    'type': current_type or 'http',
                    'country': country,
                    'ip': ip,
                    'port': port,
                    'user': user,
                    'password': password,
                    'proxy_url': proxy_url
                })
                logger.debug(f"Parsed proxy: {country} - {proxy_url}")
            else:
                logger.warning(f"Could not parse proxy line: {line}")
    
    except Exception as e:
        logger.error(f"Error parsing proxy file {file_path}: {e}")
    
    return proxies

def normalize_country_name(country: str) -> str:
    """
    Normalize country name for comparison.
    
    Args:
        country: Country name from error or proxy file
        
    Returns:
        Normalized country name (lowercase)
    """
    if not country:
        return ''
    
    country_lower = country.lower().strip()
    
    # Remove common suffixes and prefixes
    country_lower = re.sub(r'\s*\(.*?\)\s*', '', country_lower)  # Remove parentheses content
    country_lower = re.sub(r'\s*,\s*.*$', '', country_lower)  # Remove everything after comma (for "Country, State")
    country_lower = country_lower.strip()
    
    # Check mapping first
    if country_lower in COUNTRY_MAPPING:
        return COUNTRY_MAPPING[country_lower]
    
    # Try partial matching for compound names (e.g., "United States" matches "United States of America")
    for key, value in COUNTRY_MAPPING.items():
        if key in country_lower or country_lower in key:
            return value
    
    return country_lower

def extract_available_countries(error_message: str) -> Optional[List[str]]:
    """
    Extract list of available countries from YouTube error message.
    
    Args:
        error_message: Error message from yt-dlp
        
    Returns:
        List of country names if found, None otherwise
    """
    error_lower = error_message.lower()
    
    # Pattern 1: "This video is available in Canada, Japan, United States."
    pattern1 = r'this video is available in\s+([^.]+)\.'
    match1 = re.search(pattern1, error_lower, re.IGNORECASE)
    
    if match1:
        countries_text = match1.group(1)
        # Split by comma and clean up
        countries = [c.strip() for c in countries_text.split(',')]
        # Remove empty strings
        countries = [c for c in countries if c]
        if countries:
            logger.info(f"Extracted {len(countries)} available countries from error (pattern 1)")
            return countries
    
    # Pattern 2: Look for "available in" followed by a long list (may span multiple lines)
    # This handles cases where the list is very long and may include line breaks
    pattern2 = r'available in\s+([^.\n]+(?:,\s*[^.\n]+)*)'
    match2 = re.search(pattern2, error_lower, re.IGNORECASE | re.DOTALL)
    
    if match2:
        countries_text = match2.group(1)
        # Split by comma and clean up
        countries = [c.strip() for c in countries_text.split(',')]
        # Remove empty strings and limit to reasonable number (avoid parsing entire error as one country)
        countries = [c for c in countries if c and len(c) < 100]
        if 1 <= len(countries) <= 200:  # Reasonable range
            logger.info(f"Extracted {len(countries)} available countries from error (pattern 2)")
            return countries
    
    # Pattern 3: Look for "This video is available in" at the start, then extract until period or newline
    # This handles very long lists that might not match pattern 1 or 2
    pattern3 = r'this video is available in\s+([^.\n]+?)(?:\.|$)'
    match3 = re.search(pattern3, error_lower, re.IGNORECASE | re.DOTALL)
    
    if match3:
        countries_text = match3.group(1)
        # Split by comma and clean up
        countries = [c.strip() for c in countries_text.split(',')]
        # Remove empty strings and limit to reasonable number
        countries = [c for c in countries if c and len(c) < 100]
        if 1 <= len(countries) <= 200:  # Reasonable range
            logger.info(f"Extracted {len(countries)} available countries from error (pattern 3)")
            return countries
    
    return None

def find_matching_proxies(available_countries: List[str], proxy_list: List[Dict]) -> List[Dict]:
    """
    Find proxies from proxy_list that match available countries.
    
    Args:
        available_countries: List of country names from error message
        proxy_list: List of proxy dictionaries from parse_proxy_file
        
    Returns:
        List of matching proxy dictionaries, ordered by type (http first, then socks5)
    """
    matching_proxies = []
    seen_proxies = set()  # Track proxies we've already added to avoid duplicates
    
    # Normalize available countries
    normalized_available = [normalize_country_name(c) for c in available_countries]
    
    for proxy in proxy_list:
        proxy_country_normalized = normalize_country_name(proxy['country'])
        proxy_key = (proxy['ip'], proxy['port'], proxy['type'])  # Unique key for proxy
        
        # Skip if we've already added this proxy
        if proxy_key in seen_proxies:
            continue
        
        # Check if proxy country matches any available country
        for available_country in normalized_available:
            available_normalized = normalize_country_name(available_country)
            
            # Exact match
            if proxy_country_normalized == available_normalized:
                matching_proxies.append(proxy)
                seen_proxies.add(proxy_key)
                logger.debug(f"Found matching proxy: {proxy['country']} ({proxy['type']}) matches {available_country}")
                break
            # Partial match (e.g., "United States" matches "United States of America")
            elif proxy_country_normalized in available_normalized or available_normalized in proxy_country_normalized:
                matching_proxies.append(proxy)
                seen_proxies.add(proxy_key)
                logger.debug(f"Found partial matching proxy: {proxy['country']} ({proxy['type']}) partially matches {available_country}")
                break
    
    # Sort by type: http first, then socks5
    matching_proxies.sort(key=lambda x: (x['type'] != 'http', x['country']))
    
    return matching_proxies

def get_all_proxies_from_file(file_path: str = "TXT/proxy.txt") -> List[Dict]:
    """
    Get all proxies from file, ordered by type (http first, then socks5).
    
    Args:
        file_path: Path to proxy.txt file
        
    Returns:
        List of all proxy dictionaries, ordered by type
    """
    proxies = parse_proxy_file(file_path)
    
    # Sort by type: http first, then socks5
    proxies.sort(key=lambda x: (x['type'] != 'http', x['country']))
    
    return proxies
