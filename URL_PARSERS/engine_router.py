from URL_PARSERS.tags import extract_url_range_tags
from HELPERS.safe_messeger import fake_message
from HELPERS.logger import logger, send_to_logger
from COMMANDS.image_cmd import image_command, _normalize_img_url
from CONFIG.domains import DomainsConfig
from urllib.parse import urlparse


def is_gallerydl_url(url) -> bool:
    """
    True если ссылка обслуживается исключительно gallery-dl.

    Критерии те же, что у route_if_gallerydl_only (GALLERYDL_ONLY_PATH /
    GALLERYDL_ONLY_DOMAINS), но перед проверкой применяется существующая
    нормализация vk.ru -> vk.com из image_cmd, чтобы пачки vk.ru/album-...
    тоже распознавались как gallery-dl ссылки.
    """
    try:
        url = _normalize_img_url(url or '')
        url_l = url.lower()
        domain = urlparse(url).netloc.lower()
        if domain.startswith('www.'):
            domain = domain[4:]

        # 1) Абсолютное совпадение по части пути из массива GALLERYDL_ONLY_PATH
        for path_part in (getattr(DomainsConfig, 'GALLERYDL_ONLY_PATH', []) or []):
            if path_part and path_part.lower() in url_l:
                return True

        # 2) Домены из списка GALLERYDL_ONLY_DOMAINS
        for d in (getattr(DomainsConfig, 'GALLERYDL_ONLY_DOMAINS', []) or []):
            d_l = (d or '').strip().lower()
            if d_l and (domain == d_l or domain.endswith('.' + d_l)):
                return True
    except Exception as e:
        logger.error(f"[ENGINE_ROUTER] is_gallerydl_url error: {e}")
    return False


def process_admin_gallery_batch(app, message, urls, tags_text=''):
    """
    Админский мульти-URL режим для gallery-dl (#admin-multi-img).

    Сообщение без команды /img содержит несколько ссылок и все они —
    gallery-dl (vk.com/album-... и т.п.): каждая ссылка последовательно
    прогоняется через image_command как отдельная задача, со статус-сообщением
    как у process_multiple_urls_queue. Лимит количества ссылок (10) для
    админов не применяется.
    """
    from HELPERS.safe_messeger import safe_send_message, safe_edit_message_text
    from CONFIG.messages import safe_get_messages
    from pyrogram.types import ReplyParameters

    user_id = message.chat.id
    messages = safe_get_messages(user_id)

    # Лог multi-img запроса в LOGS_ID канал (как у видео-мультиURL пути)
    try:
        user_name = getattr(message.from_user, "username", None) or getattr(message.chat, "first_name", "") or ""
        log_text = f"[MULTI_URL_IMG] User: {user_name} ({user_id}) | urls: {', '.join(urls)}"
        send_to_logger(message, log_text)
    except Exception as log_e:
        logger.error(f"[ENGINE_ROUTER] Failed to log multi-img request: {log_e}")

    # Send initial status message
    total_urls = len(urls)
    status_msg_text = f"""
<b>📶 {messages.TOTAL_PROGRESS_MSG}</b>
<blockquote>{messages.URL_PROGRESS_MSG.format(current=0, total=total_urls)}</blockquote>
"""
    status_msg = safe_send_message(user_id, status_msg_text, reply_parameters=ReplyParameters(message_id=message.id))
    status_msg_id = status_msg.id if status_msg else None

    # Каждая ссылка — отдельная задача image_command. Вызываем недекорированную
    # функцию (__wrapped__), чтобы задачи шли строго последовательно в текущем
    # потоке (как down_and_up в process_multiple_urls_queue), а не уходили
    # пачкой параллельных заданий в background-пул.
    img_handler = getattr(image_command, '__wrapped__', image_command)

    # For groups, preserve original chat_id and message_thread_id (как engine_router)
    original_chat_id = getattr(getattr(message, 'chat', None), 'id', None)
    message_thread_id = getattr(message, 'message_thread_id', None) if hasattr(message, 'message_thread_id') else None

    # Process each URL sequentially
    for idx, url in enumerate(urls, 1):
        try:
            # Update status message
            if status_msg_id:
                try:
                    status_msg_text = f"""
<b>📶 {messages.TOTAL_PROGRESS_MSG}</b>
<blockquote>{messages.URL_PROGRESS_MSG.format(current=idx, total=total_urls)}</blockquote>
"""
                    safe_edit_message_text(user_id, status_msg_id, status_msg_text)
                except Exception as e:
                    logger.debug(f"Failed to update status message: {e}")

            fallback_text = f"/img {url}"
            if tags_text:
                fallback_text += f" {tags_text}"
            fake_msg = fake_message(fallback_text, message.chat.id, original_chat_id=original_chat_id,
                                    message_thread_id=message_thread_id, original_message=message)
            img_handler(app, fake_msg)
            logger.info(f"[ENGINE_ROUTER] Admin multi-img {idx}/{total_urls} done: {url}")
        except Exception as e:
            logger.error(f"[ENGINE_ROUTER] Error processing gallery URL {idx}/{total_urls} ({url}): {e}")
            continue

    # Update final status
    if status_msg_id:
        try:
            final_status = f"""
<b>📶 {messages.TOTAL_PROGRESS_MSG}</b>
<blockquote>{messages.URL_PROGRESS_MSG.format(current=total_urls, total=total_urls)}</blockquote>
✅ {messages.MULTI_URL_COMPLETED_MSG if hasattr(messages, 'MULTI_URL_COMPLETED_MSG') else 'Обработка завершена'}
"""
            safe_edit_message_text(user_id, status_msg_id, final_status)
        except Exception as e:
            logger.debug(f"Failed to update final status: {e}")

    return True


def route_if_gallerydl_only(app, message) -> bool:
    """
    Решает, нужно ли сразу маршрутизировать ссылку в gallery-dl (команда /img),
    минуя yt-dlp. Возвращает True, если обработка полностью выполнена здесь.
    """
    try:
        text = (getattr(message, 'text', None) or getattr(message, 'caption', '') or '').strip()
        if not text:
            return False

        url, _s, _e, _plist, _tags, tags_text, _err = extract_url_range_tags(text)
        if not url:
            return False

        url_l = url.lower()
        domain = urlparse(url).netloc.lower()
        if domain.startswith('www.'):
            domain = domain[4:]

        # 1) Абсолютное совпадение по части пути из массива GALLERYDL_ONLY_PATH
        try:
            path_list = getattr(DomainsConfig, 'GALLERYDL_ONLY_PATH', []) or []
        except Exception:
            path_list = []
        for path_part in path_list:
            try:
                if path_part and path_part.lower() in url_l:
                    fallback_text = f"/img {url}"
                    if tags_text:
                        fallback_text += f" {tags_text}"
                    # For groups, preserve original chat_id and message_thread_id
                    original_chat_id = getattr(getattr(message, 'chat', None), 'id', None)
                    message_thread_id = getattr(message, 'message_thread_id', None) if hasattr(message, 'message_thread_id') else None
                    fake_msg = fake_message(fallback_text, message.chat.id, original_chat_id=original_chat_id, message_thread_id=message_thread_id, original_message=message)
                    image_command(app, fake_msg)
                    logger.info(f"[ENGINE_ROUTER] Routed by path to gallery-dl: {path_part} -> {fallback_text}")
                    return True
            except Exception as e:
                logger.error(f"[ENGINE_ROUTER] Error checking path {path_part}: {e}")

        # 2) Домены из списка GALLERYDL_ONLY_DOMAINS
        try:
            domains_list = getattr(DomainsConfig, 'GALLERYDL_ONLY_DOMAINS', []) or []
        except Exception:
            domains_list = []
        for d in domains_list:
            try:
                d_l = (d or '').strip().lower()
                if not d_l:
                    continue
                if domain == d_l or domain.endswith('.' + d_l):
                    fallback_text = f"/img {url}"
                    if tags_text:
                        fallback_text += f" {tags_text}"
                    # For groups, preserve original chat_id and message_thread_id
                    original_chat_id = getattr(getattr(message, 'chat', None), 'id', None)
                    message_thread_id = getattr(message, 'message_thread_id', None) if hasattr(message, 'message_thread_id') else None
                    fake_msg = fake_message(fallback_text, message.chat.id, original_chat_id=original_chat_id, message_thread_id=message_thread_id, original_message=message)
                    image_command(app, fake_msg)
                    logger.info(f"[ENGINE_ROUTER] Routed by domain list to gallery-dl: {domain} -> {fallback_text}")
                    return True
            except Exception as e:
                logger.error(f"[ENGINE_ROUTER] Error checking domain {d}: {e}")

        return False
    except Exception as e:
        logger.error(f"[ENGINE_ROUTER] route_if_gallerydl_only error: {e}")
        return False


