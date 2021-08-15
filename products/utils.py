from functools import wraps
import jwt
from django.conf import settings
from django.http import HttpResponse


def requireLogin(to_authenticate_fn):
    @wraps(to_authenticate_fn)
    def inner(request, *args, **kwargs):
        token = request.headers.get('token',None)
        if verify_token(token):
            #check if email is present or not
            return to_authenticate_fn(request, *args, **kwargs)
        else:
            return HttpResponse('Unauthorised', status = 401)
    return inner;

def verify_token(token):
    '''    try:
        data = jwt.decode(token, settings.SECRET_KEY, algorithms='H5256')
    except:
        return None'''
    data = jwt.decode(token, settings.SECRET_KEY, algorithms='H5256')
    return {'email': data('email')}