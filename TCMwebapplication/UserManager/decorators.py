from functools import wraps
from django.contrib.auth.decorators import user_passes_test

def user_type_required(allowed_user_types):
    def decorator(view_func):
        @wraps(view_func)
        @user_passes_test(lambda u: u.user_type in allowed_user_types)
        def wrapper(request, *args, **kwargs):
            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator