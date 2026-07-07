from functools import wraps
from flask import session, redirect

def login_required_decorator(func):
    @wraps(func)
    def decorated_func(*args, **kwargs): # (arguments, keyword arguments)
        if "username" not in session:
            return redirect("/login")
        
        result = func(*args, **kwargs)
        return result
    
    return decorated_func
