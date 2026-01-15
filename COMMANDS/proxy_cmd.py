# /Proxy Command
import os
import tempfile
from pyrogram import filters
from CONFIG.config import Config
from CONFIG.messages import Messages, safe_get_messages
from CONFIG.logger_msg import LoggerMsg
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyParameters

from HELPERS.app_instance import get_app
from HELPERS.filesystem_hlp import create_directory
from HELPERS.logger import send_to_logger, logger, send_to_all
from HELPERS.safe_messeger import safe_send_message, safe_edit_message_text
from HELPERS.decorators import background_handler
from HELPERS.limitter import is_user_in_channel
from HELPERS.proxy_file_helper import parse_proxy_file

# Get app instance for decorators
app = get_app()

def safe_write_file(file_path, content):
    """Safely write content to file with atomic operation"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write to temporary file first, then rename (atomic operation)
        temp_dir = os.path.dirname(file_path)
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=temp_dir, delete=False) as temp_file:
            temp_file.write(content)
            temp_file.flush()
            temp_path = temp_file.name
        
        # Atomic rename
        os.rename(temp_path, file_path)
        return True
    except OSError as e:
        logger.error(LoggerMsg.PROXY_CMD_ERROR_WRITING_FILE_LOG_MSG.format(file_path=file_path, error=e))
        # Clean up temp file if it exists
        try:
            if 'temp_path' in locals() and os.path.exists(temp_path):
                os.unlink(temp_path)
        except Exception:
            pass
        return False
    except Exception as e:
        logger.error(LoggerMsg.PROXY_CMD_UNEXPECTED_ERROR_WRITING_FILE_LOG_MSG.format(file_path=file_path, error=e))
        return False

@app.on_message(filters.command("proxy") & filters.private)
@background_handler(label="proxy_command")
def proxy_command(app, message):
    messages = safe_get_messages(message.chat.id)
    user_id = message.chat.id
    is_admin = int(user_id) in Config.ADMIN
    
    # Check if user is ignored (even admins can be ignored, but ignore/unignore commands are always allowed) - highest priority
    text = getattr(message, 'text', '').strip() if hasattr(message, 'text') else ''
    is_ignore_command = text.startswith(Config.IGNORE_USER_COMMAND) or text.startswith(Config.UNIGNORE_USER_COMMAND)
    
    if not is_ignore_command:
        from DATABASE.firebase_init import is_user_ignored
        if is_user_ignored(message):
            return  # User is ignored, no response at all (even for admins)
    
    logger.info(LoggerMsg.PROXY_CMD_USER_REQUESTED_LOG_MSG.format(user_id=user_id))
    logger.info(LoggerMsg.PROXY_CMD_USER_IS_ADMIN_LOG_MSG.format(user_id=user_id, is_admin=is_admin))
    
    is_in_channel = is_user_in_channel(app, message)
    logger.info(LoggerMsg.PROXY_CMD_USER_IS_IN_CHANNEL_LOG_MSG.format(user_id=user_id, is_in_channel=is_in_channel))
    
    if not is_admin and not is_in_channel:
        logger.info(LoggerMsg.PROXY_CMD_USER_ACCESS_DENIED_LOG_MSG.format(user_id=user_id))
        return
    
    logger.info(LoggerMsg.PROXY_CMD_USER_ACCESS_GRANTED_LOG_MSG.format(user_id=user_id))
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    
    # Fast toggle via args: /proxy on|off
    try:
        parts = (message.text or "").split()
        if len(parts) >= 2:
            arg = parts[1].lower()
            proxy_file = os.path.join(user_dir, "proxy.txt")
            if arg in ("on", "off"):
                if arg == "on":
                    # Check if user has selected a country
                    selected_country = get_user_selected_country(user_id)
                    if selected_country:
                        # Write country code to proxy.txt
                        country_code = get_country_code(selected_country)
                        content_to_write = country_code
                    else:
                        # Write "ON" to proxy.txt
                        content_to_write = "ON"
                else:
                    # Write "OFF" to proxy.txt
                    content_to_write = "OFF"
                
                if safe_write_file(proxy_file, content_to_write):
                    if arg == "on":
                        selected_country_after = get_user_selected_country(user_id)
                        if selected_country_after:
                            msg = f"✅ Прокси включен\n🌍 Используется страна: {selected_country_after}"
                        else:
                            msg = safe_get_messages(user_id).PROXY_ENABLED_MSG.format(status='enabled')
                    else:
                        msg = safe_get_messages(user_id).PROXY_ENABLED_MSG.format(status='disabled')
                    safe_send_message(user_id, msg, message=message)
                    send_to_logger(message, safe_get_messages(user_id).PROXY_SET_COMMAND_LOG_MSG.format(arg=arg))
                    return
                else:
                    error_msg = safe_get_messages(user_id).PROXY_ERROR_SAVING_MSG
                    safe_send_message(user_id, error_msg, message=message)
                    from HELPERS.logger import log_error_to_channel
                    log_error_to_channel(message, error_msg)
                    return
    except Exception:
        pass
    
    buttons = [
        [InlineKeyboardButton(safe_get_messages(user_id).PROXY_ON_BUTTON_MSG, callback_data="proxy_option|on"), InlineKeyboardButton(safe_get_messages(user_id).PROXY_OFF_BUTTON_MSG, callback_data="proxy_option|off")],
    ]
    
    # Add country buttons from proxy file
    countries = get_countries_from_proxy_file()
    selected_country = get_user_selected_country(user_id)
    
    if countries:
        # Add header for country selection
        messages = safe_get_messages(user_id)
        buttons.append([InlineKeyboardButton(messages.PROXY_COUNTRY_SELECT_HEADER_MSG, callback_data="proxy_option|country_header")])
        
        # Add country buttons in rows of 2
        country_buttons = []
        for country in countries:
            # Add flag emoji if available, or use country name
            flag_emoji = ""
            country_display = country
            # Try to match country with flag (simplified)
            country_flags = {
                'Germany': '🇩🇪',
                'Russia': '🇷🇺',
                'United States': '🇺🇸',
                'Turkey': '🇹🇷',
                'Italy': '🇮🇹',
                'India': '🇮🇳',
                'Georgia': '🇬🇪',
                'Belarus': '🇧🇾',
                'Thailand': '🇹🇭',
                'Netherlands': '🇳🇱',
                'United Kingdom': '🇬🇧',
            }
            flag_emoji = country_flags.get(country, '🌍')
            
            # Mark selected country
            if selected_country and selected_country.lower() == country.lower():
                country_display = f"✓ {flag_emoji} {country}"
            else:
                country_display = f"{flag_emoji} {country}"
            
            country_buttons.append(InlineKeyboardButton(
                country_display,
                callback_data=f"proxy_option|country|{country}"
            ))
        
        # Add country buttons in rows of 2
        for i in range(0, len(country_buttons), 2):
            row = country_buttons[i:i+2]
            buttons.append(row)
        
        # Add button to clear country selection
        if selected_country:
            buttons.append([InlineKeyboardButton(messages.PROXY_COUNTRY_CLEAR_BUTTON_MSG, callback_data="proxy_option|country|clear")])
    
    buttons.append([InlineKeyboardButton(safe_get_messages(user_id).PROXY_CLOSE_BUTTON_MSG, callback_data="proxy_option|close")])
    
    keyboard = InlineKeyboardMarkup(buttons)
    # Get available proxy count
    configs = get_all_proxy_configs()
    proxy_count = len(configs)
    
    # Get proxy count from file
    try:
        from HELPERS.proxy_file_helper import get_all_proxies_from_file
        file_proxies = get_all_proxies_from_file("TXT/proxy.txt")
        file_count = len(file_proxies)
    except Exception:
        file_count = 0
    
    # Build message text
    if proxy_count > 0 or file_count > 0:
        proxy_text = safe_get_messages(user_id).PROXY_MENU_TEXT_MULTIPLE_MSG.format(
            config_count=proxy_count,
            file_count=file_count
        )
    else:
        proxy_text = safe_get_messages(user_id).PROXY_MENU_TEXT_MSG
    
    # Add info about selected country if any (reads from proxy.txt)
    messages = safe_get_messages(user_id)
    if selected_country:
        country_code = get_country_code(selected_country)
        proxy_text += "\n\n" + messages.PROXY_COUNTRY_SELECTED_IN_MENU_MSG.format(
            country=selected_country,
            country_code=country_code
        )
        proxies = get_proxies_for_country(selected_country)
        if proxies:
            http_count = len([p for p in proxies if p['type'] == 'http'])
            socks5_count = len([p for p in proxies if p['type'] == 'socks5'])
            proxy_text += "\n" + messages.PROXY_COUNTRY_PROXIES_AVAILABLE_MSG.format(
                proxy_count=len(proxies),
                http_count=http_count,
                socks5_count=socks5_count
            )
            # Check if proxy is enabled
            if is_proxy_enabled(user_id):
                proxy_text += "\n" + messages.PROXY_COUNTRY_ENABLED_FOR_COUNTRY_MSG
            else:
                proxy_text += "\n" + messages.PROXY_COUNTRY_DISABLED_FOR_COUNTRY_MSG
    
    # Add info about available countries
    if countries:
        proxy_text += "\n\n" + safe_get_messages(user_id).PROXY_COUNTRY_AVAILABLE_COUNTRIES_MSG.format(count=len(countries))
    
    safe_send_message(
        user_id,
        proxy_text,
        reply_markup=keyboard,
        message=message
    )
    send_to_logger(message, safe_get_messages(user_id).PROXY_MENU_OPENED_LOG_MSG)


@app.on_callback_query(filters.regex(r"^proxy_option\|"))
def proxy_option_callback(app, callback_query):
    user_id = callback_query.from_user.id
    messages = safe_get_messages(user_id)
    logger.info(LoggerMsg.PROXY_CMD_CALLBACK_LOG_MSG.format(callback_data=callback_query.data))
    parts = callback_query.data.split("|")
    data = parts[1] if len(parts) > 1 else ""
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    proxy_file = os.path.join(user_dir, "proxy.txt")
    
    if callback_query.data == "proxy_option|close":
        try:
            callback_query.message.delete()
        except Exception:
            callback_query.edit_message_reply_markup(reply_markup=None)
        try:
            callback_query.answer(safe_get_messages(user_id).PROXY_MENU_CLOSED_MSG)
        except Exception:
            pass
        send_to_logger(callback_query.message, safe_get_messages(user_id).PROXY_MENU_CLOSED_LOG_MSG)
        return
    
    # Handle country selection
    if data == "country" and len(parts) > 2:
        country = parts[2]
        
        if country == "clear":
            # Clear country selection
            if set_user_selected_country(user_id, None):
                messages = safe_get_messages(user_id)
                try:
                    callback_query.answer(messages.PROXY_COUNTRY_CLEARED_CALLBACK_MSG)
                except Exception:
                    pass
                # Close menu
                try:
                    callback_query.message.delete()
                except Exception:
                    pass
                # Send confirmation message
                safe_send_message(
                    callback_query.message.chat.id,
                    messages.PROXY_COUNTRY_CLEARED_MSG,
                    message=callback_query.message
                )
            return
        
        if country == "header":
            # Just a header button, do nothing
            try:
                callback_query.answer()
            except Exception:
                pass
            return
        
        # Set selected country - writes country code to proxy.txt
        if set_user_selected_country(user_id, country):
            proxies = get_proxies_for_country(country)
            proxy_count = len(proxies)
            http_count = len([p for p in proxies if p['type'] == 'http'])
            socks5_count = len([p for p in proxies if p['type'] == 'socks5'])
            country_code = get_country_code(country)
            
            # Build confirmation message using translations
            messages = safe_get_messages(user_id)
            message_text = messages.PROXY_COUNTRY_SELECTED_MSG.format(
                country=country,
                country_code=country_code
            )
            message_text += "\n" + messages.PROXY_COUNTRY_PROXIES_AVAILABLE_MSG.format(
                proxy_count=proxy_count,
                http_count=http_count,
                socks5_count=socks5_count
            )
            message_text += "\n" + messages.PROXY_COUNTRY_TRY_ORDER_MSG
            message_text += "\n" + messages.PROXY_COUNTRY_AUTO_ENABLED_MSG
            
            # Close menu
            try:
                callback_query.message.delete()
            except Exception:
                pass
            
            # Send confirmation message
            safe_send_message(
                callback_query.message.chat.id,
                message_text,
                message=callback_query.message
            )
            
            send_to_logger(callback_query.message, f"User {user_id} selected proxy country: {country} (code: {country_code})")
            try:
                callback_query.answer(messages.PROXY_COUNTRY_SELECTED_CALLBACK_MSG.format(country=country))
            except Exception:
                pass
            return
    
    if data == "on":
        # Check if user has selected a country
        selected_country = get_user_selected_country(user_id)
        
        if selected_country:
            # User has selected a country - write country code to proxy.txt
            country_code = get_country_code(selected_country)
            if not safe_write_file(proxy_file, country_code):
                try:
                    callback_query.answer(safe_get_messages(user_id).PROXY_ERROR_SAVING_CALLBACK_MSG)
                except Exception:
                    pass
                return
        else:
            # No country selected - write "ON" to proxy.txt
            if not safe_write_file(proxy_file, "ON"):
                try:
                    callback_query.answer(safe_get_messages(user_id).PROXY_ERROR_SAVING_CALLBACK_MSG)
                except Exception:
                    pass
                return
        
        # Get available proxy count and selection method
        configs = get_all_proxy_configs()
        proxy_count = len(configs)
        
        # Check if user has selected a country (re-read after writing)
        messages = safe_get_messages(user_id)
        selected_country_after = get_user_selected_country(user_id)
        if selected_country_after:
            proxies = get_proxies_for_country(selected_country_after)
            if proxies:
                http_count = len([p for p in proxies if p['type'] == 'http'])
                socks5_count = len([p for p in proxies if p['type'] == 'socks5'])
                message_text = messages.PROXY_ENABLED_CONFIRM_MSG + "\n"
                message_text += messages.PROXY_COUNTRY_FROM_FILE_MSG.format(country=selected_country_after) + "\n"
                message_text += messages.PROXY_COUNTRY_PROXIES_AVAILABLE_MSG.format(
                    proxy_count=len(proxies),
                    http_count=http_count,
                    socks5_count=socks5_count
                )
            else:
                if proxy_count and proxy_count > 1:
                    message_text = messages.PROXY_ENABLED_MULTIPLE_MSG.format(count=proxy_count, method=Config.PROXY_SELECT)
                else:
                    message_text = messages.PROXY_ENABLED_CONFIRM_MSG
        else:
            # ALL AUTO mode - show info about Config + file proxies
            try:
                from HELPERS.proxy_file_helper import get_all_proxies_from_file
                file_proxies = get_all_proxies_from_file("TXT/proxy.txt")
                file_count = len(file_proxies)
            except Exception:
                file_count = 0
            
            if proxy_count > 0 or file_count > 0:
                message_text = messages.PROXY_ENABLED_ALL_AUTO_MSG.format(
                    config_count=proxy_count,
                    file_count=file_count
                )
            elif proxy_count and proxy_count > 1:
                message_text = messages.PROXY_ENABLED_MULTIPLE_MSG.format(count=proxy_count, method=Config.PROXY_SELECT)
            else:
                message_text = messages.PROXY_ENABLED_CONFIRM_MSG
        
        # Close menu
        try:
            callback_query.message.delete()
        except Exception:
            pass
        
        # Send confirmation message
        safe_send_message(
            callback_query.message.chat.id,
            message_text,
            message=callback_query.message
        )
        
        send_to_logger(callback_query.message, messages.PROXY_ENABLED_LOG_MSG)
        try:
            callback_query.answer(messages.PROXY_ENABLED_CALLBACK_MSG)
        except Exception:
            pass
        return
    
    if data == "off":
        if not safe_write_file(proxy_file, "OFF"):
            try:
                callback_query.answer(safe_get_messages(user_id).PROXY_ERROR_SAVING_CALLBACK_MSG)
            except Exception:
                pass
            return
        
        messages = safe_get_messages(user_id)
        
        # Close menu
        try:
            callback_query.message.delete()
        except Exception:
            pass
        
        # Send confirmation message
        safe_send_message(
            callback_query.message.chat.id,
            messages.PROXY_DISABLED_MSG,
            message=callback_query.message
        )
        
        send_to_logger(callback_query.message, messages.PROXY_DISABLED_LOG_MSG)
        try:
            callback_query.answer(messages.PROXY_DISABLED_CALLBACK_MSG)
        except Exception:
            pass
        return


def is_proxy_enabled(user_id):
    """Check if proxy is enabled for user (returns True if ON or country code)"""
    user_dir = os.path.join("users", str(user_id))
    proxy_file = os.path.join(user_dir, "proxy.txt")
    if not os.path.exists(proxy_file):
        return False
    try:
        with open(proxy_file, "r", encoding="utf-8") as f:
            content = f.read().strip().upper()
            # Check if it's "ON" or a country code (2 letters)
            if content == "ON":
                return True
            # Check if it's a valid country code (2-3 letters)
            if len(content) >= 2 and len(content) <= 3 and content.isalpha():
                # Verify it's a known country code
                country = get_country_by_code(content)
                if country:
                    return True
            return False
    except OSError as e:
        logger.error(LoggerMsg.PROXY_CMD_ERROR_READING_FILE_LOG_MSG.format(proxy_file=proxy_file, error=e))
        return False
    except Exception as e:
        logger.error(LoggerMsg.PROXY_CMD_UNEXPECTED_ERROR_READING_FILE_LOG_MSG.format(proxy_file=proxy_file, error=e))
        return False


def get_proxy_config():
    """Get proxy configuration from config"""
    return {
        'type': Config.PROXY_TYPE,
        'ip': Config.PROXY_IP,
        'port': Config.PROXY_PORT,
        'user': Config.PROXY_USER,
        'password': Config.PROXY_PASSWORD
    }

def get_proxy_2_config():
    """Get second proxy configuration from config"""
    return {
        'type': Config.PROXY_2_TYPE,
        'ip': Config.PROXY_2_IP,
        'port': Config.PROXY_2_PORT,
        'user': Config.PROXY_2_USER,
        'password': Config.PROXY_2_PASSWORD
    }

def get_all_proxy_configs():
    """Get all available proxy configurations"""
    configs = []
    
    # First proxy
    if hasattr(Config, 'PROXY_TYPE') and hasattr(Config, 'PROXY_IP') and hasattr(Config, 'PROXY_PORT'):
        if Config.PROXY_IP and Config.PROXY_PORT:
            configs.append({
                'type': Config.PROXY_TYPE,
                'ip': Config.PROXY_IP,
                'port': Config.PROXY_PORT,
                'user': Config.PROXY_USER,
                'password': Config.PROXY_PASSWORD
            })
    
    # Second proxy
    if hasattr(Config, 'PROXY_2_TYPE') and hasattr(Config, 'PROXY_2_IP') and hasattr(Config, 'PROXY_2_PORT'):
        if Config.PROXY_2_IP and Config.PROXY_2_PORT:
            configs.append({
                'type': Config.PROXY_2_TYPE,
                'ip': Config.PROXY_2_IP,
                'port': Config.PROXY_2_PORT,
                'user': Config.PROXY_2_USER,
                'password': Config.PROXY_2_PASSWORD
            })
    
    return configs

def select_proxy_for_user():
    """Select proxy for user based on PROXY_SELECT method"""
    import random
    
    configs = get_all_proxy_configs()
    if not configs:
        return None
    
    if len(configs) == 1:
        return configs[0]
    
    # Select method based on PROXY_SELECT
    if hasattr(Config, 'PROXY_SELECT') and Config.PROXY_SELECT == "random":
        return random.choice(configs)
    else:  # default to round_robin
        # Simple round-robin using a global counter
        if not hasattr(select_proxy_for_user, 'counter'):
            select_proxy_for_user.counter = 0
        selected = configs[select_proxy_for_user.counter % len(configs)]
        select_proxy_for_user.counter += 1
        return selected


def build_proxy_url(proxy_config):
    """Build proxy URL from configuration"""
    if not proxy_config or 'type' not in proxy_config or 'ip' not in proxy_config or 'port' not in proxy_config:
        return None
    
    if proxy_config['type'] == 'http':
        if proxy_config.get('user') and proxy_config.get('password'):
            return f"http://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
        else:
            return f"http://{proxy_config['ip']}:{proxy_config['port']}"
    elif proxy_config['type'] == 'https':
        if proxy_config.get('user') and proxy_config.get('password'):
            return f"https://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
        else:
            return f"https://{proxy_config['ip']}:{proxy_config['port']}"
    elif proxy_config['type'] in ['socks4', 'socks5', 'socks5h']:
        if proxy_config.get('user') and proxy_config.get('password'):
            return f"{proxy_config['type']}://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
        else:
            return f"{proxy_config['type']}://{proxy_config['ip']}:{proxy_config['port']}"
    else:
        if proxy_config.get('user') and proxy_config.get('password'):
            return f"http://{proxy_config['user']}:{proxy_config['password']}@{proxy_config['ip']}:{proxy_config['port']}"
        else:
            return f"http://{proxy_config['ip']}:{proxy_config['port']}"

def select_proxy_for_domain(url):
    """Select appropriate proxy for domain based on PROXY_DOMAINS and PROXY_2_DOMAINS"""
    from CONFIG.domains import DomainsConfig
    
    # Extract domain from URL
    domain = None
    if '://' in url:
        domain = url.split('://')[1].split('/')[0]
    else:
        domain = url.split('/')[0]
    
    logger.info(LoggerMsg.PROXY_CMD_SELECT_PROXY_FOR_DOMAIN_LOG_MSG.format(url=url, domain=domain))
    logger.info(LoggerMsg.PROXY_CMD_PROXY_2_DOMAINS_LOG_MSG.format(domains=getattr(DomainsConfig, 'PROXY_2_DOMAINS', [])))
    logger.info(LoggerMsg.PROXY_CMD_PROXY_DOMAINS_LOG_MSG.format(domains=getattr(DomainsConfig, 'PROXY_DOMAINS', [])))
    
    # Helper function to check if domain matches any domain in the list (including subdomains)
    def is_domain_in_list(domain, domain_list):
        """Check if domain or any of its subdomains match entries in domain_list"""
        if not domain_list:
            return False
        
        # Direct match
        if domain in domain_list:
            return True
        
        # Check if any domain in the list is a subdomain of the current domain
        for listed_domain in domain_list:
            if domain.endswith('.' + listed_domain) or domain == listed_domain:
                return True
        
        return False
    
    # Check PROXY_2_DOMAINS first
    if hasattr(DomainsConfig, 'PROXY_2_DOMAINS') and DomainsConfig.PROXY_2_DOMAINS:
        if is_domain_in_list(domain, DomainsConfig.PROXY_2_DOMAINS):
            logger.info(LoggerMsg.PROXY_CMD_DOMAIN_FOUND_IN_PROXY_2_LOG_MSG.format(domain=domain))
            return get_proxy_2_config()
    
    # Check PROXY_DOMAINS
    if hasattr(DomainsConfig, 'PROXY_DOMAINS') and DomainsConfig.PROXY_DOMAINS:
        if is_domain_in_list(domain, DomainsConfig.PROXY_DOMAINS):
            logger.info(LoggerMsg.PROXY_CMD_DOMAIN_FOUND_IN_PROXY_1_LOG_MSG.format(domain=domain))
            return get_proxy_config()
    
    logger.info(LoggerMsg.PROXY_CMD_DOMAIN_NOT_IN_LIST_LOG_MSG.format(domain=domain))
    return None

def resolve_proxy_config(user_id=None, url=None, allow_domain_fallback=True):
    """
    Determine which proxy configuration should be used for the current context.
    Priority:
    1. User-selected country from proxy file (if proxy is enabled)
    2. User-specific proxy toggle (/proxy on) - uses config proxies
    3. Domain-specific proxy lists (if enabled and allowed)
    """
    reason = None
    proxy_config = None
    
    if user_id is not None:
        try:
            proxy_enabled = is_proxy_enabled(user_id)
            logger.info(LoggerMsg.PROXY_CMD_PROXY_CHECK_FOR_USER_LOG_MSG.format(user_id=user_id, proxy_enabled=proxy_enabled))
            if proxy_enabled:
                # Check if user has selected a country from proxy file (reads from proxy.txt)
                selected_country = get_user_selected_country(user_id)
                if selected_country:
                    # User selected country - return None here, will be handled by get_proxy_url_for_user_country
                    logger.info(f"User {user_id} has selected country {selected_country} from proxy.txt")
                    return None, "country_file"
                
                # Fallback to config-based proxy
                proxy_config = select_proxy_for_user()
                reason = "user"
        except Exception as e:
            logger.warning(LoggerMsg.PROXY_CMD_ERROR_CHECKING_PROXY_LOG_MSG.format(user_id=user_id, error=e))
    
    if proxy_config is None and allow_domain_fallback and url:
        proxy_config = select_proxy_for_domain(url)
        if proxy_config:
            reason = "domain"
    
    return proxy_config, reason


def get_proxy_url(user_id=None, url=None, allow_domain_fallback=True):
    """Return proxy URL string for current context or None."""
    proxy_config, reason = resolve_proxy_config(user_id, url, allow_domain_fallback)
    
    # If user selected a country from proxy file, use that
    if reason == "country_file" and user_id:
        country_proxy_url, _ = get_proxy_url_for_user_country(user_id)
        if country_proxy_url:
            return country_proxy_url, "country_file"
    
    if not proxy_config:
        return None, None
    proxy_url = build_proxy_url(proxy_config)
    if not proxy_url:
        return None, None
    return proxy_url, reason


def get_requests_proxies(user_id=None, url=None, allow_domain_fallback=True):
    """
    Build a proxies dict suitable for requests when proxy mode is enabled.
    Returns dict or None.
    """
    proxy_url, reason = get_proxy_url(user_id, url, allow_domain_fallback)
    if not proxy_url:
        return None, None
    proxies = {
        'http': proxy_url,
        'https': proxy_url,
        'HTTP': proxy_url,
        'HTTPS': proxy_url,
    }
    return proxies, reason


def get_country_code(country: str) -> str:
    """Get ISO country code for country name"""
    country_codes = {
        'Germany': 'DE',
        'Russia': 'RU',
        'United States': 'US',
        'Turkey': 'TR',
        'Italy': 'IT',
        'India': 'IN',
        'Georgia': 'GE',
        'Belarus': 'BY',
        'Thailand': 'TH',
        'Netherlands': 'NL',
        'United Kingdom': 'GB',
    }
    return country_codes.get(country, country.upper()[:2] if len(country) >= 2 else country.upper())

def get_country_by_code(code: str) -> str:
    """Get country name by ISO country code"""
    code_to_country = {
        'DE': 'Germany',
        'RU': 'Russia',
        'US': 'United States',
        'TR': 'Turkey',
        'IT': 'Italy',
        'IN': 'India',
        'GE': 'Georgia',
        'BY': 'Belarus',
        'TH': 'Thailand',
        'NL': 'Netherlands',
        'GB': 'United Kingdom',
    }
    return code_to_country.get(code.upper())

def get_countries_from_proxy_file():
    """Get unique list of countries from TXT/proxy.txt file"""
    proxies = parse_proxy_file("TXT/proxy.txt")
    countries = sorted(set(proxy['country'] for proxy in proxies))
    return countries

def get_proxies_for_country(country: str):
    """Get all proxies (HTTP and SOCKS5) for a specific country from TXT/proxy.txt"""
    proxies = parse_proxy_file("TXT/proxy.txt")
    country_proxies = [p for p in proxies if p['country'].lower() == country.lower()]
    # Sort: HTTP first, then SOCKS5
    country_proxies.sort(key=lambda x: (x['type'] != 'http', x['country']))
    return country_proxies

def get_user_selected_country(user_id):
    """Get user's selected country from proxy.txt file (checks for country code)"""
    user_dir = os.path.join("users", str(user_id))
    proxy_file = os.path.join(user_dir, "proxy.txt")
    if not os.path.exists(proxy_file):
        return None
    try:
        with open(proxy_file, "r", encoding="utf-8") as f:
            content = f.read().strip().upper()
            # If it's "ON" or "OFF", no country selected
            if content in ("ON", "OFF"):
                return None
            # Check if it's a country code
            if len(content) >= 2 and len(content) <= 3 and content.isalpha():
                country = get_country_by_code(content)
                if country:
                    return country
            return None
    except Exception as e:
        logger.error(f"Error reading proxy file for user {user_id}: {e}")
        return None

def set_user_selected_country(user_id, country):
    """Set user's selected country - writes country code to proxy.txt"""
    user_dir = os.path.join("users", str(user_id))
    create_directory(user_dir)
    proxy_file = os.path.join(user_dir, "proxy.txt")
    try:
        if country:
            # Get country code and write to proxy.txt
            country_code = get_country_code(country)
            with open(proxy_file, "w", encoding="utf-8") as f:
                f.write(country_code)
            logger.info(f"Set proxy country code {country_code} for user {user_id} (country: {country})")
        else:
            # Clear country selection - write "OFF" to proxy.txt
            with open(proxy_file, "w", encoding="utf-8") as f:
                f.write("OFF")
            logger.info(f"Cleared proxy country for user {user_id}")
        return True
    except Exception as e:
        logger.error(f"Error writing proxy file for user {user_id}: {e}")
        return False

def get_proxy_url_for_user_country(user_id):
    """Get proxy URL for user's selected country (tries HTTP first, then SOCKS5)"""
    user_selected_country = get_user_selected_country(user_id)
    if not user_selected_country:
        return None, None
    
    proxies = get_proxies_for_country(user_selected_country)
    if not proxies:
        logger.warning(f"No proxies found for country {user_selected_country}")
        return None, None
    
    # Return first proxy (HTTP if available, otherwise SOCKS5)
    return proxies[0]['proxy_url'], user_selected_country

def add_proxy_to_ytdl_opts(ytdl_opts, url, user_id=None, allow_domain_fallback=True):
    """Add proxy to yt-dlp options if proxy is enabled for user or domain requires it"""
    logger.info(LoggerMsg.PROXY_CMD_ADD_PROXY_CALLED_LOG_MSG.format(user_id=user_id, url=url))
    
    # First check if user has selected a country from proxy file
    if user_id:
        country_proxy_url, selected_country = get_proxy_url_for_user_country(user_id)
        if country_proxy_url:
            ytdl_opts['proxy'] = country_proxy_url
            logger.info(f"Using proxy from file for country {selected_country}: {country_proxy_url}")
            return ytdl_opts
    
    # Fallback to config-based proxy
    proxy_url, reason = get_proxy_url(user_id=user_id, url=url, allow_domain_fallback=allow_domain_fallback)
    if proxy_url:
        ytdl_opts['proxy'] = proxy_url
        if reason == "user":
            logger.info(LoggerMsg.PROXY_CMD_ADDED_PROXY_FOR_USER_LOG_MSG.format(user_id=user_id, proxy_url=proxy_url))
        else:
            logger.info(LoggerMsg.PROXY_CMD_ADDED_DOMAIN_PROXY_LOG_MSG.format(url=url, proxy_url=proxy_url))
    
    return ytdl_opts
