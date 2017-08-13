"""
This package will be called by the Skipole framework to access your data.
"""

# this import used by basic authentication
from base64 import b64decode

from .. import FailPage, GoTo, ValidateError, ServerError


from . import widgets, login, responders

##############################################################################
#
# Your code needs to provide your own version of the following functions
#
##############################################################################


def start_project(project, projectfiles, path, option):
    """On a project being loaded, and before the wsgi service is started, this is called once,
          and should return a dictionary (typically an empty dictionary if this value is not used).
           This function can be used to set any initial parameters, and the dictionary returned will
           be passed as 'proj_data' to subsequent start_call functions."""
    proj_data = {}
    return proj_data


def start_call(environ, path, project, called_ident, caller_ident, received_cookies, ident_data, lang, option, proj_data):
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

    if submit_list and (submit_list[0] == 'responders'):
        # expects submitlist to have contents such as ['responders', 'submitdata', 'test1']
        # where package 'responders' contains module 'submitdata' containing function 'test1' to be run as the submit_data function
        try:
            respondersmod = getattr(responders, submit_list[1])
        except:
            raise FailPage("submit_list contains 'responders' but module not recognised")
        try:
            submitfunc = getattr(respondersmod, submit_list[2])
        except:
            raise FailPage("submit_list contains 'responders' and '%s', but function not recognised" % (submit_list[1],))
        return submitfunc(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang)


    raise FailPage("submit_list string not recognised")


_HEADER_TEXT = { 2001 : "Skipole tests.",
                 3001:"Widget Modules",
                 3002: "The checkbox module.",
                 3003: "The confirm module.",
                 3006: "The paras module.",
                 3007: "The links module.",
                 3008: "The error_messages module.",
                 3009: "The inputforms module",
                 3010: "The inputtext module",
                 3011: "The info module",
                 3012: "The debug_tools module",
                 3013: "The dropdown module",
                 3014: "The footers module",
                 3015: "The headers module",
                 3016: "The inputtables module",
                 3017: "The radio module",
                 3018: "The svgarrows module",
                 3019: "The svgbasics module",
                 3020: "The tables module",
                 3021: "The textarea module",
                 3022: "The upload module",
                14002:"Tests for the CheckBox1 widget.",
                14010:"Tests for the CheckBox2 widget.",
                14020:"Tests for the CheckedText widget.",
                14101:"Tests for the Table1_Button widget.",
                14201:"Tests for the ErrorDiv widget",
                14210:"Tests for the ErrorPara widget",
                14220:"Tests for the ErrorClear1 widget.",
                14230:"Tests for the ErrorClear2 widget.",
                14301:"Tests for the ServerTimeStamp widget.",
                14401:"Tests for the AlertClear1 widget.",
                14410:"Tests for the ConfirmBox1 widget.",
                14420:"Tests for the ConfirmBox2 widget.",
                14601:"Tests for the TextInput1 widget.",
                14610:"Tests for the TextInput2 widget.",
                14620:"Tests for the TextInput3 widget.",
                14630:"Tests for the TextInput4 widget.",
               100101:"Tests using a cookie to login",
               100102:"Secure 1 page",
               100104:"Secure 2 page",
               100106:"Secure 3 page",
               200001:"Responders"}

_NAV_BUTTONS = {  3001:[['home','Home', False, '']],
                  3002:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3003:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3006:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3007:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3008:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3009:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3010:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3011:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3012:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3013:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3014:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3015:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3016:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3017:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3018:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3019:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3020:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3021:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3022:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                 14002:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['checkbox', 'checkbox', False, '']],
                 14010:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['checkbox', 'checkbox', False, '']],
                 14020:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['checkbox', 'checkbox', False, '']],
                 14101:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['links', 'links', False, '']],
                 14201:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['error_messages', 'error_messages', False, '']],
                 14210:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['error_messages', 'error_messages', False, '']],
                 14220:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['error_messages', 'error_messages', False, '']],
                 14230:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['error_messages', 'error_messages', False, '']],
                 14301:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['info', 'info', False, '']],
                 14401:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['confirm', 'confirm', False, '']],
                 14410:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['confirm', 'confirm', False, '']],
                 14420:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['confirm', 'confirm', False, '']],
                 14601:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputtext', 'inputtext', False, '']],
                 14610:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputtext', 'inputtext', False, '']],
                 14620:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputtext', 'inputtext', False, '']],
                 14630:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputtext', 'inputtext', False, '']],
                100101:[['home','Home', False, '']],
                100102:[['home','Home', False, ''], ['login','Test Login', False, '']],
                100104:[['home','Home', False, ''], ['login','Test Login', False, '']],
                100106:[['home','Home', False, ''], ['login','Test Login', False, '']],
                200001:[['home','Home', False, '']]}

def end_call(page_ident, page_type, call_data, page_data, proj_data, lang):
    """This function is called at the end of a call prior to filling the returned page with page_data,
       it can also return an optional ident_data string to embed into forms."""
    if page_type != "TemplatePage":
        return
    page_num = page_ident[1]
    if page_num in _HEADER_TEXT:
        page_data['header', 'headpara', 'para_text']  = _HEADER_TEXT[page_num]
    if page_num in _NAV_BUTTONS:
        page_data['navigation', 'navbuttons', 'nav_links'] = _NAV_BUTTONS[page_num]
    if 'status' in call_data:
        page_data['foot','foot_status','footer_text'] = call_data['status']

    # set secure1 cookie
    if 'session' in call_data:
        return call_data['session']


