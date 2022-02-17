def allow_access():
    def decorator(func):
        setattr(func, 'allow', True)
        return func

    return decorator
