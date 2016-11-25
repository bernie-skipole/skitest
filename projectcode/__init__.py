"""
This package will be called by the Skipole framework to access your data.
"""

# this import used by basic authentication
from base64 import b64decode

from ...skilift import FailPage, GoTo, ValidateError, ServerError


from . import widgets, login

##############################################################################
#
# Your code needs to provide your own version of the following functions
#
##############################################################################

def start_call(environ, path, project, called_ident, caller_ident, received_cookies, ident_data, lang, check, proj_data):
    "When a call is initially received this function is called."
    if not called_ident:
        # return unknown url
        return None, {}, {}, lang
    call_data = {'project':project, 'received_cookies':received_cookies}
    page_data = {}
    # for basic auth, if access to secure3 via 100007 does not have password, return 100107 instead
    if (called_ident[1] == 100007):
        # check user allowed to go to secure page 3
        auth = environ.get('HTTP_AUTHORIZATION')
        if auth:
            scheme, data = auth.split(" ", 1)
            assert scheme.lower() == 'basic'
            username, password = b64decode(data).decode('UTF-8').split(':', 1)
            if len(username) > 3 and password == "password3":
                # login ok
                call_data['USERNAME'] = username
                return called_ident, call_data, page_data, lang
        # login fail, request a login
        return (project,100107), call_data, page_data, lang
    return called_ident, call_data, page_data, lang


def submit_data(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    "This function is called when a Responder wishes to submit data for processing in some manner"

    if submit_list and (submit_list[0] == 'widgets'):
        # expects submitlist to have contents such as ['widgets', 'checkbox', 'test1']
        # where package 'widgets' contains module 'checkbox' containing function 'test1' to be run as the submit_data function
        try:
            widgetmod = getattr(widgets, submit_list[1])
        except:
            raise FailPage("submit_list contains 'widgets' but module not recognised")
        try:
            submitfunc = getattr(widgetmod, submit_list[2])
        except:
            raise FailPage("submit_list contains 'widgets' and '%s', but function not recognised" % (submit_list[1],))
        return submitfunc(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang)

    if submit_list and (submit_list[0] == 'login'):
        try:
            submitfunc = getattr(login, submit_list[1])
        except:
            raise FailPage("submit_list contains 'login', but function not recognised")
        return submitfunc(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang)

    raise FailPage("submit_list string not recognised")


_HEADER_TEXT = { 2001 : "skipole web framework tests.",
                                         3001:"Widget Modules",
                                         3002: "The checkbox module.",
                                         3003: "The confirm module.",
                                         3006: "The paras module.",
                                         3007: "The links module.",
                                         5002:"Tests for the CheckBox1 widget.",
                                         5010:"Tests for the CheckBox2 widget.",
                                         5020:"Tests for the CheckedText widget.",
                                         5101:"Tests for the Table1_Button widget.",
                                    100101:"Tests using a cookie to login",
                                    100102:"Secure 1 page",
                                    100104:"Secure 2 page",
                                    100106:"Secure 3 page"}

_NAV_BUTTONS = {3001:[['home','Home', False, '']],
                                          3002:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                                          3003:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                                          3006:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                                          3007:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                                          5002:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['checkbox', 'checkbox', False, '']],
                                          5010:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['checkbox', 'checkbox', False, '']],
                                          5020:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['checkbox', 'checkbox', False, '']],
                                          5101:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['links', 'links', False, '']],
                                     100101:[['home','Home', False, '']],
                                     100102:[['home','Home', False, ''], ['login','Test Login', False, '']],
                                     100104:[['home','Home', False, ''], ['login','Test Login', False, '']],
                                     100106:[['home','Home', False, ''], ['login','Test Login', False, '']]}

def end_call(page_ident, call_data, page_data, proj_data, lang):
    """This function is called at the end of a call prior to filling the returned page with page_data,
       it can also return an optional ident_data string to embed into forms."""
    if page_ident is None:
        return
    page_num = page_ident[1]
    if page_num in _HEADER_TEXT:
        page_data['header', 'headpara', 'para_text']  = _HEADER_TEXT[page_num]
    if page_num in _NAV_BUTTONS:
        page_data['navigation', 'navbuttons', 'nav_links'] = _NAV_BUTTONS[page_num]
    return
