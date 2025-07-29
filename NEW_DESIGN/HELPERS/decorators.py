# Decorators for automatic app usage
from functools import wraps
from HELPERS.app_instance import get_app_lazy

def app_handler(func):
    """Decorator to automatically inject app instance"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # If first argument is not app, inject it
        if args and hasattr(args[0], 'send_message'):
            # First argument is already app
            return func(*args, **kwargs)
        else:
            # Inject app as first argument
            app = get_app_lazy()
            return func(app, *args, **kwargs)
    return wrapper

def on_message(filters=None):
    """Decorator factory for message handlers"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            app = get_app_lazy()
            if app:
                # Register the handler with the app
                app.on_message(filters)(func)
            return func
        return wrapper
    return decorator 