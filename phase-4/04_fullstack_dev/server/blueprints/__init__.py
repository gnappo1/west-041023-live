from flask import request, Blueprint, make_response, abort, g, session
from marshmallow import ValidationError
from flask_restful import Resource
from functools import wraps

def login_required(func):
    @wraps(func) #* This is a decorator that will preserve the information about the original function (name, docstring, etc.)
    def decorated_function(*args, **qwargs):
        if 'user_id' not in session:
            abort(401, 'Unauthorized')
        return func(*args, **qwargs)
    return decorated_function