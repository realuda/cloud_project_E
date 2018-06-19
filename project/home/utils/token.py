import hashlib
import datetime

def set_cookie(response, key, value, days_expire = 7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(max_age), "%a, %d-%b-%Y %H: %M:%S GMT")
    response.set_cookie(key, value)
    return response

def check_token(request):
    if request.COOKIES.get('khustagram_login') is not None:
        return True
    else:
        return False
