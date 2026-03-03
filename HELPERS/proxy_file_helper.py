"""
Helper module for working with proxy list from TXT/proxy.txt file
"""
import os
import re
import logging
from typing import List, Dict, Optional, Tuple, Callable

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
    'united arab emirates': 'united arab emirates',
    'uae': 'united arab emirates',
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
            
            # Check for section headers (including "HTTP(S) (online):" and "SOCKS5 (online):")
            if line.upper().startswith('HTTP'):
                current_type = 'http'
                continue
            elif line.upper().startswith('SOCKS5'):
                current_type = 'socks5'
                continue
            
            # Parse proxy line: 🇩🇪 Germany – 1.2.3.4:8080:username:password  or  🇩🇪 Germany – 1.2.3.4:8080  (no auth)
            # Format: [flag] Country – IP:PORT[:USER:PASSWORD]  (user/password optional for no-auth proxies)
            match = re.match(r'[^\w]*([A-Za-z\s]+?)\s*[–-]\s*(\d+\.\d+\.\d+\.\d+):(\d+):([^:]*):(.*)', line)
            if match:
                country = match.group(1).strip()
                ip = match.group(2)
                port = match.group(3)
                user = (match.group(4) or '').strip()
                password = (match.group(5) or '').strip()
                if current_type == 'socks5':
                    proxy_url = f"socks5://{user}:{password}@{ip}:{port}" if (user or password) else f"socks5://{ip}:{port}"
                else:
                    proxy_url = f"http://{user}:{password}@{ip}:{port}" if (user or password) else f"http://{ip}:{port}"
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
                # No-auth format: 🇩🇪 Germany – 1.2.3.4:8080
                match_no_auth = re.match(r'[^\w]*([A-Za-z\s]+?)\s*[–-]\s*(\d+\.\d+\.\d+\.\d+):(\d+)\s*$', line)
                if match_no_auth:
                    country = match_no_auth.group(1).strip()
                    ip = match_no_auth.group(2)
                    port = match_no_auth.group(3)
                    if current_type == 'socks5':
                        proxy_url = f"socks5://{ip}:{port}"
                    else:
                        proxy_url = f"http://{ip}:{port}"
                    proxies.append({
                        'type': current_type or 'http',
                        'country': country,
                        'ip': ip,
                        'port': port,
                        'user': '',
                        'password': '',
                        'proxy_url': proxy_url
                    })
                    logger.debug(f"Parsed proxy (no auth): {country} - {proxy_url}")
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

def test_proxy_url(proxy_url: str, timeout: int = 5) -> bool:
    """
    Test if proxy is reachable (one quick request). Used before download to skip dead proxies.
    Returns True if proxy responds, False otherwise.
    """
    if not proxy_url:
        return False
    try:
        import requests
        proxies = {"http": proxy_url, "https": proxy_url}
        r = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=timeout)
        return r.status_code == 200
    except Exception:
        return False


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


# Extended ISO 3166-1 alpha-2 code -> country name (for ip-api and menu)
# Used so get_country_by_code/get_country_code work for any country from online proxy list
ISO_CODE_TO_COUNTRY_NAME: Dict[str, str] = {
    "AD": "Andorra", "AE": "United Arab Emirates", "AF": "Afghanistan", "AG": "Antigua and Barbuda",
    "AL": "Albania", "AM": "Armenia", "AO": "Angola", "AR": "Argentina", "AT": "Austria", "AU": "Australia",
    "AZ": "Azerbaijan", "BA": "Bosnia and Herzegovina", "BB": "Barbados", "BD": "Bangladesh", "BE": "Belgium",
    "BF": "Burkina Faso", "BG": "Bulgaria", "BH": "Bahrain", "BI": "Burundi", "BJ": "Benin", "BN": "Brunei",
    "BO": "Bolivia", "BR": "Brazil", "BS": "Bahamas", "BT": "Bhutan", "BW": "Botswana", "BY": "Belarus",
    "BZ": "Belize", "CA": "Canada", "CD": "Democratic Republic of the Congo", "CF": "Central African Republic",
    "CG": "Republic of the Congo", "CH": "Switzerland", "CI": "Côte d'Ivoire", "CL": "Chile", "CM": "Cameroon",
    "CN": "China", "CO": "Colombia", "CR": "Costa Rica", "CU": "Cuba", "CV": "Cape Verde", "CY": "Cyprus",
    "CZ": "Czech Republic", "DE": "Germany", "DJ": "Djibouti", "DK": "Denmark", "DO": "Dominican Republic",
    "DZ": "Algeria", "EC": "Ecuador", "EE": "Estonia", "EG": "Egypt", "ER": "Eritrea", "ES": "Spain",
    "ET": "Ethiopia", "FI": "Finland", "FJ": "Fiji", "FR": "France", "GA": "Gabon", "GB": "United Kingdom",
    "GE": "Georgia", "GH": "Ghana", "GM": "Gambia", "GN": "Guinea", "GQ": "Equatorial Guinea", "GR": "Greece",
    "GT": "Guatemala", "GW": "Guinea-Bissau", "GY": "Guyana", "HK": "Hong Kong", "HN": "Honduras", "HR": "Croatia", "HT": "Haiti",
    "HU": "Hungary", "ID": "Indonesia", "IE": "Ireland", "IL": "Israel", "IN": "India", "IQ": "Iraq",
    "IR": "Iran", "IS": "Iceland", "IT": "Italy", "JM": "Jamaica", "JO": "Jordan", "JP": "Japan",
    "KE": "Kenya", "KG": "Kyrgyzstan", "KH": "Cambodia", "KM": "Comoros", "KN": "Saint Kitts and Nevis",
    "KP": "North Korea", "KR": "South Korea", "KW": "Kuwait", "KZ": "Kazakhstan", "LA": "Laos",
    "LB": "Lebanon", "LC": "Saint Lucia", "LI": "Liechtenstein", "LK": "Sri Lanka", "LR": "Liberia",
    "LS": "Lesotho", "LT": "Lithuania", "LU": "Luxembourg", "LV": "Latvia", "LY": "Libya", "MA": "Morocco",
    "MD": "Moldova", "ME": "Montenegro", "MG": "Madagascar", "MK": "North Macedonia", "ML": "Mali",
    "MM": "Myanmar", "MN": "Mongolia", "MR": "Mauritania", "MT": "Malta", "MU": "Mauritius", "MV": "Maldives",
    "MW": "Malawi", "MX": "Mexico", "MY": "Malaysia", "MZ": "Mozambique", "NA": "Namibia", "NE": "Niger",
    "NG": "Nigeria", "NI": "Nicaragua", "NL": "Netherlands", "NO": "Norway", "NP": "Nepal", "NZ": "New Zealand",
    "OM": "Oman", "PA": "Panama", "PE": "Peru", "PG": "Papua New Guinea", "PH": "Philippines", "PK": "Pakistan",
    "PL": "Poland", "PR": "Puerto Rico", "PT": "Portugal", "PY": "Paraguay", "QA": "Qatar", "RO": "Romania", "RS": "Serbia",
    "RU": "Russia", "RW": "Rwanda", "SA": "Saudi Arabia", "SB": "Solomon Islands", "SC": "Seychelles",
    "SD": "Sudan", "SE": "Sweden", "SG": "Singapore", "SI": "Slovenia", "SK": "Slovakia", "SL": "Sierra Leone",
    "SN": "Senegal", "SO": "Somalia", "SR": "Suriname", "SS": "South Sudan", "SV": "El Salvador", "SY": "Syria",
    "SZ": "Eswatini", "TD": "Chad", "TG": "Togo", "TH": "Thailand", "TJ": "Tajikistan", "TM": "Turkmenistan",
    "TN": "Tunisia", "TR": "Turkey", "TT": "Trinidad and Tobago", "TW": "Taiwan", "TZ": "Tanzania",
    "UA": "Ukraine", "UG": "Uganda", "UK": "United Kingdom", "US": "United States", "UY": "Uruguay",
    "UZ": "Uzbekistan", "VE": "Venezuela", "VN": "Vietnam", "VU": "Vanuatu", "XK": "Kosovo", "YE": "Yemen",
    "ZA": "South Africa", "ZM": "Zambia", "ZW": "Zimbabwe",
}


def get_country_name_by_code_extended(code: str) -> Optional[str]:
    """Return country name for ISO code (for extended list from online proxies)."""
    if not code:
        return None
    return ISO_CODE_TO_COUNTRY_NAME.get((code or "").upper()[:2])


def get_country_code_by_name_extended(name: str) -> Optional[str]:
    """Return ISO code for country name (for extended list from online proxies)."""
    if not name:
        return None
    name_clean = (name or "").strip()
    if name_clean.lower().startswith("the "):
        name_clean = name_clean[4:].strip()
    for code, cname in ISO_CODE_TO_COUNTRY_NAME.items():
        if cname.lower() == name_clean.lower():
            return code
    return None


def country_code_to_flag(code: str) -> str:
    """Convert ISO 3166-1 alpha-2 country code to emoji flag (e.g. DE -> 🇩🇪)."""
    if not code or len(code) < 2:
        return "🌍"
    code = code.upper()[:2]
    return "".join(chr(ord(c) + 127397) for c in code)


def get_country_by_ip(ip: str, cache: Optional[Dict[str, Tuple[str, str]]] = None,
                      timeout: float = 5.0) -> Tuple[str, str]:
    """
    Resolve country name and code by IP using ip-api.com (no key, 45 req/min).
    Returns (country_name, country_code), e.g. ("Germany", "DE").
    Uses cache dict if provided (mutated in place).
    """
    if cache is not None and ip in cache:
        v = cache[ip]
        return (v[0], v[1]) if isinstance(v, (list, tuple)) and len(v) >= 2 else v
    result = ("Unknown", "XX")
    try:
        import requests
        r = requests.get(
            f"http://ip-api.com/json/{ip}?fields=country,countryCode",
            timeout=timeout
        )
        if r.status_code == 200:
            data = r.json()
            country = data.get("country") or "Unknown"
            code = (data.get("countryCode") or "XX")[:2]
            result = (country, code.upper())
    except Exception as e:
        logger.debug(f"Geo lookup for {ip}: {e}")
    if cache is not None:
        cache[ip] = list(result)
    return result


def parse_working_proxy_line(line: str) -> Optional[Dict]:
    """
    Parse a line from working_proxies.txt (e.g. socks5://185.65.202.186:1080).
    Returns dict with keys: protocol ('http'|'socks4'|'socks5'), host, port; or None if invalid.
    """
    line = (line or "").strip()
    if not line or line.startswith("#"):
        return None
    match = re.match(r"(?i)(https?|socks[45]h?):\/\/([^:\s]+):(\d+)", line)
    if not match:
        return None
    protocol = match.group(1).lower()
    host = match.group(2).strip()
    port = match.group(3)
    if protocol in ("https", "http"):
        ptype = "http"
    elif protocol in ("socks4", "socks5", "socks5h"):
        ptype = "socks5"
    else:
        return None
    return {"protocol": protocol, "host": host, "port": port, "type": ptype}


def merge_working_proxies_to_proxy_file(
    working_proxies_path: str = "TXT/working_proxies.txt",
    proxy_path: str = "TXT/proxy.txt",
    geo_cache_path: str = "TXT/.proxy_geo_cache.json",
    delay_between_geo: float = 1.5,
    progress_callback: Optional[Callable[[int, int, str], None]] = None,
) -> Tuple[int, int]:
    """
    Read working_proxies.txt, resolve country per IP (with cache), write proxy.txt format to proxy_path.
    Replaces the entire "HTTP(S) (online):" / "SOCKS5 (online):" block with the current working_proxies
    content — so when working_proxies.txt is updated (e.g. every 30 min), old merged proxies that are
    no longer in the file are removed from proxy.txt; only current working proxies remain.
    progress_callback: optional callable(current_index, total, host) for progress output.
    Returns (count_http, count_socks5) written.
    """
    import time
    import json
    if not os.path.exists(working_proxies_path):
        logger.debug(f"merge_working_proxies: {working_proxies_path} not found, skip (optional)")
        return 0, 0
    geo_cache = {}
    if os.path.exists(geo_cache_path):
        try:
            with open(geo_cache_path, "r", encoding="utf-8") as f:
                geo_cache = json.load(f)
        except Exception:
            pass
    try:
        with open(working_proxies_path, "r", encoding="utf-8") as f:
            raw_lines = f.readlines()
    except Exception as e:
        logger.error(f"merge_working_proxies: read {working_proxies_path}: {e}")
        return 0, 0
    parsed = []
    for line in raw_lines:
        info = parse_working_proxy_line(line)
        if info:
            parsed.append(info)
    if not parsed:
        return 0, 0
    total = len(parsed)
    all_entries = []
    for i, p in enumerate(parsed):
        if progress_callback:
            try:
                progress_callback(i + 1, total, p.get("host", ""))
            except Exception:
                pass
        host = p["host"]
        was_in_cache = host in geo_cache
        country, code = get_country_by_ip(host, cache=geo_cache)
        if not was_in_cache:
            time.sleep(delay_between_geo)
        flag = country_code_to_flag(code)
        line_fmt = f"{flag} {country} – {p['host']}:{p['port']}"
        all_entries.append((p["type"], line_fmt))
    # Save geo cache (values as lists for JSON)
    try:
        os.makedirs(os.path.dirname(geo_cache_path) or ".", exist_ok=True)
        with open(geo_cache_path, "w", encoding="utf-8") as f:
            json.dump(geo_cache, f, ensure_ascii=False)
    except Exception as e:
        logger.debug(f"merge_working_proxies: write geo cache: {e}")
    # Read proxy.txt: keep only lines before the first "online" block (manual proxies/headers)
    # Everything from "HTTP(S) (online):" / "SOCKS5 (online):" to EOF is discarded and replaced below
    manual_lines = []
    if os.path.exists(proxy_path):
        try:
            with open(proxy_path, "r", encoding="utf-8") as f:
                for line in f:
                    if re.match(r"^\s*HTTP\s*\(.*\)\s*\(online\)", line, re.I) or re.match(r"^\s*SOCKS5\s*\(online\)", line, re.I):
                        break
                    manual_lines.append(line.rstrip("\n"))
        except Exception as e:
            logger.error(f"merge_working_proxies: read proxy.txt: {e}")
            manual_lines = []
    # Build new content: manual + online sections
    while manual_lines and manual_lines[-1].strip() == "":
        manual_lines.pop()
    lines_out = list(manual_lines)
    if lines_out:
        lines_out.append("")
    lines_out.append("HTTP(S) (online):")
    for t, line_fmt in all_entries:
        if t == "http":
            lines_out.append(line_fmt)
    lines_out.append("")
    lines_out.append("SOCKS5 (online):")
    for t, line_fmt in all_entries:
        if t == "socks5":
            lines_out.append(line_fmt)
    try:
        os.makedirs(os.path.dirname(proxy_path) or ".", exist_ok=True)
        with open(proxy_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines_out) + "\n")
    except Exception as e:
        logger.error(f"merge_working_proxies: write proxy.txt: {e}")
        return 0, 0
    count_http = sum(1 for t, _ in all_entries if t == "http")
    count_socks5 = sum(1 for t, _ in all_entries if t == "socks5")
    logger.info(f"merge_working_proxies: wrote {count_http} HTTP + {count_socks5} SOCKS5 online proxies to {proxy_path}")
    return count_http, count_socks5
