# Global app instance
# This module provides a global app instance that can be imported by other modules

from CONFIG.messages import Messages, safe_get_messages

app = None

def set_app(app_instance):
    """Set the global app instance"""
    global app
    app = app_instance

def get_app():
    """Get the global app instance"""
    return app

def get_app_lazy():
    messages = safe_get_messages(None)
    """Get app instance with lazy loading - returns a proxy that will work when app is set"""
    class AppProxy:
        def __getattr__(self, name):
            messages = safe_get_messages(None)
            if app is None:
                raise RuntimeError(messages.APP_INSTANCE_NOT_INITIALIZED_MSG.format(name=name))
            return getattr(app, name)
    
    return AppProxy()


def safe_create_task(coro, loop=None, name=None):
    """Create an asyncio task that never loses its exception (issue #462).

    Fire-and-forget tasks created with bare ``loop.create_task(...)`` /
    ``asyncio.create_task(...)`` only surface exceptions at GC time as
    "Task exception was never retrieved" with a truncated stack. This helper
    attaches a done-callback that logs the full exception instead, while still
    never propagating it to the caller.
    """
    import asyncio
    try:
        from HELPERS.logger import logger
    except Exception:
        import logging as _logging
        logger = _logging.getLogger(__name__)
    try:
        if loop is None:
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:
                loop = asyncio.get_event_loop()
        task = loop.create_task(coro)
        if name:
            try:
                task.set_name(name)
            except Exception:
                pass

        def _log_task_exception(t):
            if t.cancelled():
                return
            exc = t.exception()
            if exc is not None:
                _task_name = name or getattr(t, "get_name", lambda: "?")()
                logger.error(
                    f"Background task '{_task_name}' failed: {type(exc).__name__}: {exc}",
                    exc_info=exc,
                )

        task.add_done_callback(_log_task_exception)
        return task
    except Exception as exc:
        logger.error(f"safe_create_task failed to schedule task: {exc}")
        # Close the coroutine to avoid "never awaited" warnings
        try:
            coro.close()
        except Exception:
            pass
        return None