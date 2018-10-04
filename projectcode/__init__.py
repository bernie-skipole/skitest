"""
This package will be called by the Skipole framework to access your data.
"""

import os

# this import used by basic authentication
from base64 import b64decode

from .. import FailPage, GoTo, ValidateError, ServerError, use_submit_list
from ... import skilift


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

    # Set environ variable for Yale Bright star catalogue
    # this is required for testing the starchart widget
    os.environ["BSC_PATH"] = "/home/bernie/test"
    return proj_data


def start_call(environ, path, project, called_ident, caller_ident, received_cookies, ident_data, lang, option, proj_data):
    "When a call is initially received this function is called."
    if not called_ident:
        # return unknown url
        return None, {}, {}, lang

    # These are sub-project tests
    if called_ident[1] == 400002:
        return "lib,test1", {}, {}, lang
    if called_ident[1] == 400003:
        return "http://www.bbc.co.uk", {}, {}, lang

    # store the project name and any cookies in the call_data dictionary
    call_data = {'project':project,
                 'received_cookies':received_cookies}
    page_data = {}

    # for basic auth, if access to secure3 via 100007 does not have password, return 100107 instead
    if called_ident[1] == 100007:
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


@use_submit_list
def submit_data(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """This function is called when a Responder wishes to submit data for processing in some manner
       For two or more submit_list values, the decorator ensures the matching function is called instead"""

    # Show the server error page
    if submit_list and (submit_list[0] == 'server_error'):
        raise ServerError(message="This is a deliberate error to show the ServerError page", code=666)
    raise ServerError("submit_list string not recognised")



_HEADER_TEXT = { 2001 : "Project skitest.",
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
                 3016: "The inputtables module",
                 3017: "The radio module",
                 3018: "The svgmeters module",
                 3019: "The svgbasics module",
                 3020: "The tables module",
                 3021: "The textarea module",
                 3022: "The upload module",
                 3023: "The logins module",
                 3025: "The lists module",
                 3026: "The svggraphs module",
                13001:"Widget Modules",
                14002:"Tests for the CheckBox1 widget.",
                14010:"Tests for the CheckBox2 widget.",
                14020:"Tests for the CheckedText widget.",
                14101:"Tests for the Table1_Button widget.",
                14105:"Tests for the MessageButton widget.",
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
                14640:"Tests for the Password1 widget.",
                14650:"Tests for the Password2 widget.",
                14660:"Tests for the SubmitTextInput1 widget.",
                14670:"Tests for the SubmitTextInput3 widget.",
                14680:"Tests for the TwoInputsSubmit1 widget.",
                14690:"Tests for the SubmitDict1 widget.",
                14701:"Tests for the HiddenField widget.",
                14801:"Tests for the TagBlock widget.",
                15001:"Tests for the UList1 widget.",
                15101:"Tests for the Chart1 widget.",
                15105:"Tests for the StarChart widget.",
                15201:"Tests for the Vertical1 widget.",
                15203:"Tests for the Traditional1 widget.",
                15401: "The headers module",
                15501:"Tests for the NamePasswd1 widget.",
               100101:"Tests using a cookie to login",
               100102:"Secure 1 page",
               100104:"Secure 2 page",
               100106:"Secure 3 page",
               210001:"Responders",
               300001:"Validator Modules",
               300002:"Basic Validators",
               300003:"Tests for the AllowedValuesOnly Validator",
               410001:"Tests for diversions to sub project pages",
               500101:"Tests of jquery UI widgets"
               }

_NAV_BUTTONS = {
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
                  3016:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3017:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3018:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3019:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3020:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3021:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3022:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3023:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3025:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                  3026:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                 13001:[['home','Home', False, '']],
                 14002:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['checkbox', 'checkbox', False, '']],
                 14010:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['checkbox', 'checkbox', False, '']],
                 14020:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['checkbox', 'checkbox', False, '']],
                 14101:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['links', 'links', False, '']],
                 14105:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['links', 'links', False, '']],
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
                 14640:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputtext', 'inputtext', False, '']],
                 14650:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputtext', 'inputtext', False, '']],
                 14660:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputtext', 'inputtext', False, '']],
                 14670:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputtext', 'inputtext', False, '']],
                 14680:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputtext', 'inputtext', False, '']],
                 14690:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputtext', 'inputtext', False, '']],
                 14701:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['inputforms', 'inputforms', False, '']],
                 14801:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['paras', 'paras', False, '']],
                 15001:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['lists', 'lists', False, '']],
                 15101:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['svggraphs', 'svggraphs', False, '']],
                 15105:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['svggraphs', 'svggraphs', False, '']],
                 15201:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['svgmeters', 'svgmeters', False, '']],
                 15203:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['svgmeters', 'svgmeters', False, '']],
                 15401:[['home','Home', False, ''], ['modules', 'Modules', False, '']],
                 15501:[['home','Home', False, ''], ['modules', 'Modules', False, ''],['logins', 'logins', False, '']],
                100101:[['home','Home', False, '']],
                100102:[['home','Home', False, ''], ['login','Test Login', False, '']],
                100104:[['home','Home', False, ''], ['login','Test Login', False, '']],
                100106:[['home','Home', False, ''], ['login','Test Login', False, '']],
                210001:[['home','Home', False, '']],
                300001:[['home','Home', False, '']],
                300002:[['home','Home', False, ''], ['valtests','Modules', False, '']],
                300003:[['home','Home', False, ''], ['valtests','Modules', False, ''], ['basictests','Basic', False, '']],
                410001:[['home','Home', False, '']],
                500101:[['home','Home', False, '']]
                }

def end_call(page_ident, page_type, call_data, page_data, proj_data, lang):
    """This function is called at the end of a call prior to filling the returned page with page_data,
       it can also return an optional ident_data string to embed into forms."""
    if page_type != "TemplatePage":
        return
    page_num = page_ident[1]
    # Insert header text into the template page
    if page_num in _HEADER_TEXT:
        page_data['header', 'headpara', 'para_text']  = _HEADER_TEXT[page_num]
    # Insert navigation links into the template page
    if page_num in _NAV_BUTTONS:
        page_data['navigation', 'navbuttons', 'nav_links'] = _NAV_BUTTONS[page_num]
    # Insert a status message into the footer if call_data['status'] is given
    if 'status' in call_data:
        page_data['foot','foot_status','footer_text'] = call_data['status']
    if page_num == 500101:
        # If this is the page of jquery UI tests, add the required javascript
        page_data['add_jscript'] = """
$( "#date" ).datepicker();
"""
    # set secure1 cookie
    if 'session' in call_data:
        return call_data['session']



