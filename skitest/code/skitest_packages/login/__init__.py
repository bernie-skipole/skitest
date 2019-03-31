
from http import cookies

from skipole import FailPage, GoTo, ValidateError, ServerError


def check_login1(skicall):
    """Raises an error if invalid password received for secure1 page"""
    if (('passwd1','input_text') in skicall.call_data) and (skicall.call_data['passwd1','input_text'] == 'password1'):
        return
    skicall.page_data['passwd1', 'set_input_errored'] = True
    raise FailPage(message="Login Failed")


def set_cookie1(skicall):
    """set cookie for access to secure1"""
    skicall.call_data['session'] = 'secure1'


def secure1_access(skicall):
    """Raises an error if no valid cookie received for secure1 page"""
    received_cookies = skicall.received_cookies
    project = skicall.project
    if project not in received_cookies:
        raise FailPage(message="You are not logged in")
    if received_cookies[project] != "secure1":
        raise FailPage(message="You are not logged in")


def secure1_logout(skicall):
    """set cookie which will not give access to secure1"""
    skicall.call_data['session'] = 'noaccess'


def check_login2(skicall):
    """Raises an error if invalid password received for secure2 page"""
    if (('passwd2','input_text') in skicall.call_data) and (skicall.call_data['passwd2','input_text'] == 'password2'):
        return
    skicall.page_data['passwd2', 'set_input_errored'] = True
    raise FailPage(message="Login Failed")


def set_cookie2(skicall):
    """set cookie for access to secure2"""
    # set a cookie 'project2:secure2'
    project = skicall.project +"2"
    cki = cookies.SimpleCookie()
    cki[project] = "secure2"
    # one minute expirey time
    cki[project]['max-age'] = 60
    return cki


def secure2_access(skicall):
    """Raises an error if no valid cookie received for secure2 page"""
    received_cookies = skicall.received_cookies
    project = skicall.project + "2"
    if project not in received_cookies:
        raise FailPage(message="You are not logged in")
    if received_cookies[project] != "secure2":
        raise FailPage(message="You are not logged in")


def secure2_logout(skicall):
    """set cookie which will not give access to secure2"""
    # set a cookie 'project2:noaccess'
    project = skicall.project
    cki = cookies.SimpleCookie()
    cki[project +"2"] = "noaccess"
    return cki


def request_login3(skicall):
    """Set up the basic authentication"""
    skicall.page_data['headers'] = [
            ('content-type', 'text/html'),
            ('WWW-Authenticate', 'Basic realm="secure3"')]
    skicall.page_data['status'] = '401 Unauthorized'


def setup_secure3(skicall):
    """Places username into the secure page"""
    if 'USERNAME' in skicall.call_data:
        skicall.page_data['show_username', 'para_text'] = "Hi there! Your username is " + skicall.call_data['USERNAME'] + "."
