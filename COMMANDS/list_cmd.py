# ####################################################################################
# List Command - Get available formats for video URL
# ####################################################################################

from HELPERS.safe_messeger import safe_callback_answer
import os
import tempfile
from html import escape
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from HELPERS.app_instance import get_app
from HELPERS.logger import logger, send_to_user, send_error_to_user, sanitize_error_message
from HELPERS.limitter import is_user_in_channel
from HELPERS.safe_messeger import safe_send_message
from HELPERS.decorators import background_handler, message_has_url
from CONFIG.config import Config
from CONFIG.messages import safe_get_messages
from CONFIG.logger_msg import LoggerMsg

# Get app instance
app = get_app()

def _format_filesize_list(filesize):
    if not filesize:
        return ''
    if filesize >= 1024 * 1024 * 1024:
        return f"{filesize / (1024*1024*1024):.2f}GiB"
    elif filesize >= 1024 * 1024:
        return f"{filesize / (1024*1024):.2f}MiB"
    elif filesize >= 1024:
        return f"{filesize / 1024:.2f}KiB"
    else:
        return f"{filesize:.0f}B"

def run_ytdlp_list(url: str, user_id: int, include_formats=False):
    """
    Get available formats using yt-dlp Python API (get_video_formats).
    Uses the same engine as Always Ask Menu for consistent results
    (PO token, js_runtimes, proxy, cookies with fallbacks).
    Returns (success, formatted_output)
    """
    def result(success, output, formats=None):
        if include_formats:
            return success, output, formats or []
        return success, output

    try:
        from DOWN_AND_UP.yt_dlp_hook import get_video_formats
        
        logger.info(f"Getting formats via Python API for user {user_id}, URL: {url}")
        info = get_video_formats(url, user_id)
        
        if not info:
            return result(False, "No video info returned")
        
        if isinstance(info, dict) and 'error' in info:
            error = info.get('error', 'Unknown error')
            return result(False, f"Error: {error}")
        
        formats = info.get('formats', [])
        if not formats:
            return result(False, "No formats found")
        
        video_id = info.get('id', 'unknown')
        title = info.get('title', 'Unknown')
        
        lines = []
        lines.append(f"[info] Available formats for {video_id}:")
        lines.append(f"Title: {title}")
        lines.append("")
        lines.append(f"{'ID':<12} {'EXT':<6} {'RESOLUTION':<14} {'FPS':>4} {'CH':>2} │ {'FILESIZE':>12} {'TBR':>7} {'PROTO':<8} │ {'VCODEC':<16} {'ACODEC':<14} {'MORE INFO'}")
        lines.append("─" * 120)
        
        for fmt in formats:
            fid = fmt.get('format_id') or ''
            if not fid or fid.startswith('[') or fid.startswith('('):
                continue
            
            ext = fmt.get('ext') or 'unknown'
            vcodec = fmt.get('vcodec') or 'none'
            acodec = fmt.get('acodec') or 'none'
            
            if vcodec == 'none' and acodec != 'none':
                resolution = 'audio only'
            elif vcodec != 'none' and acodec == 'none':
                resolution = (fmt.get('resolution') or (f"{fmt.get('width')}x{fmt.get('height')}" if fmt.get('width') and fmt.get('height') else 'unknown')) + ' (video only)'
            else:
                resolution = fmt.get('resolution') or 'unknown'
            
            fps = fmt.get('fps')
            fps_str = str(int(fps)) if fps else ''
            
            filesize = fmt.get('filesize') or fmt.get('filesize_approx')
            filesize_str = _format_filesize_list(filesize)
            
            tbr = fmt.get('tbr')
            tbr_str = f"{int(tbr)}k" if tbr else ''
            
            proto = fmt.get('protocol') or ''
            
            more_info_parts = []
            language = fmt.get('language')
            if language:
                more_info_parts.append(f"[{language}]")
            format_note = fmt.get('format_note') or ''
            if format_note:
                more_info_parts.append(format_note)
            more_info = ' '.join(more_info_parts)
            
            ch = ''
            if fmt.get('audio_channels'):
                ch = str(fmt['audio_channels'])
            
            line = f"{str(fid):<12} {str(ext):<6} {str(resolution):<14} {str(fps_str):>4} {str(ch):>2} │ {str(filesize_str):>12} {str(tbr_str):>7} {str(proto):<8} │ {str(vcodec):<16} {str(acodec):<14} {str(more_info)}"
            lines.append(line)
        
        lines.append("─" * 120)
        lines.append(f"Total: {len(formats)} formats")
        
        logger.info(f"Got {len(formats)} formats via Python API for user {user_id}")
        return result(True, '\n'.join(lines), formats)
        
    except Exception as e:
        logger.error(f"Error getting formats via Python API: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return result(False, str(e))

def _list_format_ids(formats):
    """Classify format IDs using extractor metadata, not rendered table text."""
    audio, video = [], []
    for fmt in formats:
        fid = str(fmt.get('format_id') or '')
        if not fid or fid.startswith(('[', '(')):
            continue
        vcodec = fmt.get('vcodec') or 'none'
        acodec = fmt.get('acodec') or 'none'
        if vcodec == 'none' and acodec != 'none':
            audio.append(fid)
        elif vcodec != 'none' and acodec == 'none':
            video.append(fid)
    return audio, video


def _list_caption(url, hint):
    """Keep captions safely below Telegram's 1024 UTF-16-unit limit."""
    # URL and localized hint are user-controlled/unbounded; 200 characters of
    # each stay below the limit even when every character uses two UTF-16 units.
    return f"<code>{escape(url[:200])}</code>\n{escape(hint[:200])}"


@app.on_message(filters.command("list") & filters.private)
@background_handler(label="list_command", heavy_if=message_has_url)
def list_command(app, message):
    """Handle /list command"""
    user_id = message.chat.id
    
    # Subscription check for non-admins
    if int(user_id) not in Config.ADMIN and not is_user_in_channel(app, message):
        return  # is_user_in_channel already sends subscription message
    
    # Parse command arguments
    processing_msg = None
    temp_file_path = None
    try:
        parts = message.text.strip().split(maxsplit=1)
        if len(parts) < 2:
            # Show help message
            help_text = (
safe_get_messages(user_id).LIST_HELP_MSG
            )
            keyboard = InlineKeyboardMarkup([[
                InlineKeyboardButton(safe_get_messages(user_id).LIST_CLOSE_BUTTON_MSG, callback_data="list_help|close")
            ]])
            safe_send_message(
                user_id,
                help_text,
                reply_markup=keyboard,
                message=message
            )
            return
        
        url = parts[1].strip()
        
        # Basic URL validation
        if not (url.startswith("http://") or url.startswith("https://")):
            send_error_to_user(message, safe_get_messages(user_id).LIST_INVALID_URL_MSG)
            return
        
        # Send processing message
        processing_msg = safe_send_message(
            user_id,
safe_get_messages(user_id).LIST_PROCESSING_MSG,
            message=message
        )
        
        # Run yt-dlp list command
        success, output, formats = run_ytdlp_list(url, user_id, include_formats=True)
        
        if success:
            audio_only_formats, video_only_formats = _list_format_ids(formats)

            # Create temporary file with output
            with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as temp_file:
                temp_file_path = temp_file.name
                temp_file.write(safe_get_messages(user_id).LIST_AVAILABLE_FORMATS_HEADER_MSG.format(url=url) + "\n")
                temp_file.write("=" * 50 + "\n\n")
                temp_file.write(output)
                temp_file.write("\n\n" + "=" * 50 + "\n")
                temp_file.write(safe_get_messages(user_id).LIST_HOW_TO_USE_FORMAT_IDS_TITLE)
                temp_file.write(safe_get_messages(user_id).LIST_FORMAT_USAGE_INSTRUCTIONS)
                temp_file.write(safe_get_messages(user_id).LIST_FORMAT_EXAMPLE_401)
                temp_file.write(safe_get_messages(user_id).LIST_FORMAT_EXAMPLE_401_SHORT)
                temp_file.write(safe_get_messages(user_id).LIST_FORMAT_EXAMPLE_140_AUDIO)
                temp_file.write(safe_get_messages(user_id).LIST_FORMAT_EXAMPLE_140_AUDIO_SHORT)
                
                if video_only_formats:
                    temp_file.write("\nVideo-only format IDs: " + ', '.join(video_only_formats) + "\n")
                # Add special note for audio-only formats
                if audio_only_formats:
                    temp_file.write(f"\n{safe_get_messages(user_id).LIST_AUDIO_FORMATS_DETECTED.format(formats=', '.join(audio_only_formats))}")
                    temp_file.write(safe_get_messages(user_id).LIST_AUDIO_FORMATS_NOTE)
                
            
            try:
                # Send the file
                caption = _list_caption(url, safe_get_messages(user_id).LIST_USE_FORMAT_ID_MSG)

                app.send_document(
                    user_id,
                    document=temp_file_path,
                    file_name=safe_get_messages(user_id).LIST_FORMATS_FILE_NAME_MSG.format(user_id=user_id),
                    caption=caption,
                    reply_to_message_id=message.id
                )
                
            except Exception as e:
                logger.error(f"Error sending formats file: {e}")
                send_error_to_user(message, safe_get_messages(user_id).LIST_ERROR_SENDING_MSG.format(error=str(e)))
            finally:
                # Clean up temporary file
                try:
                    os.unlink(temp_file_path)
                except Exception:
                    pass
        else:
            # Маскируем секретные данные (прокси с логином/паролем) перед отправкой пользователю
            sanitized_output = sanitize_error_message(output)
            send_error_to_user(message, safe_get_messages(user_id).LIST_ERROR_GETTING_MSG.format(error=sanitized_output))
            
    except Exception as e:
        logger.error(f"Error in list command: {e}")
        send_error_to_user(message, safe_get_messages(user_id).LIST_ERROR_OCCURRED_MSG)
    finally:
        if processing_msg:
            try:
                processing_msg.delete()
            except Exception:
                pass
        if temp_file_path:
            try:
                os.unlink(temp_file_path)
            except OSError:
                pass

@app.on_callback_query(filters.regex("^list_help\\|"))
def list_help_callback(app, callback_query):
    user_id = callback_query.from_user.id
    """Handle list help callback"""
    try:
        data = callback_query.data.split("|")[1]
        if data == "close":
            callback_query.message.delete()
            safe_callback_answer(callback_query, safe_get_messages(user_id).HELP_CLOSED_MSG)
    except Exception as e:
        logger.error(LoggerMsg.LIST_ERROR_IN_HELP_CALLBACK_LOG_MSG.format(e=e))
        safe_callback_answer(callback_query, safe_get_messages(user_id).LIST_ERROR_CALLBACK_MSG, show_alert=True)
