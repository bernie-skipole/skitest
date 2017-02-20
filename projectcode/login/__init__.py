
from http import cookies

from ....skilift import FailPage, GoTo, ValidateError, ServerError


def check_login1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error if invalid password received for secure1 page"""
    if (('passwd1','input_text') in call_data) and (call_data['passwd1','input_text'] == 'password1'):
        return
    page_data['passwd1', 'set_input_errored'] = True
    raise FailPage(message="Login Failed")


def set_cookie1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """set cookie for access to secure1"""
    call_data['session'] = 'secure1'


def secure1_access(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error if no valid cookie received for secure1 page"""
    received_cookies = call_data['received_cookies']
    project = call_data['project']
    if project not in received_cookies:
        raise FailPage(message="You are not logged in")
    if received_cookies[project] != "secure1":
        raise FailPage(message="You are not logged in")


def secure1_logout(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """set cookie which will not give access to secure1"""
    call_data['session'] = 'noaccess'


def check_login2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error if invalid password received for secure2 page"""
    if (('passwd2','input_text') in call_data) and (call_data['passwd2','input_text'] == 'password2'):
        return
    page_data['passwd2', 'set_input_errored'] = True
    raise FailPage(message="Login Failed")


def set_cookie2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """set cookie for access to secure2"""
    # set a cookie 'project2:secure2'
    project = call_data['project'] +"2"
    cki = cookies.SimpleCookie()
    cki[project] = "secure2"
    # one minute expirey time
    cki[project]['max-age'] = 60
    return cki


def secure2_access(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error if no valid cookie received for secure2 page"""
    received_cookies = call_data['received_cookies']
    project = call_data['project'] + "2"
    if project not in received_cookies:
        raise FailPage(message="You are not logged in")
    if received_cookies[project] != "secure2":
        raise FailPage(message="You are not logged in")


def secure2_logout(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """set cookie which will not give access to secure2"""
    # set a cookie 'project2:noaccess'
    project = call_data['project']
    cki = cookies.SimpleCookie()
    cki[project +"2"] = "noaccess"
    return cki


def request_login3(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Set up the basic authentication"""
    failtext = 'Please Authenticate\n'
    page_data['headers'] = [
            ('content-type', 'text/plain'),
            ('content-length', str(len(failtext))),
            ('WWW-Authenticate', 'Basic realm="secure3"')]
    page_data['status'] = '401 Unauthorized'
    return failtext


def setup_secure3(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Places username into the secure page"""
    if 'USERNAME' in call_data:
        page_data['show_username', 'para_text'] = "Hi there! Your username is " + call_data['USERNAME'] + "."
