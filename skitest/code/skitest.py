
"""
A test website to illustrate skipole widgets
"""

import os, sys

from importlib import import_module
import pkgutil

# this import used by basic authentication
from base64 import b64decode


from skipole import WSGIApplication, skis, FailPage, GoTo, ValidateError, ServerError, set_debug, use_submit_list

# the framework needs to know the location of the projectfiles directory holding this and
# other projects

PROJECTFILES = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
PROJECT = 'skitest'



def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    if not called_ident:
        # return unknown url
        return

    # These are sub-project tests
    if called_ident[1] == 400002:
        return "skis,test1"
    if called_ident[1] == 400003:
        return "http://www.bbc.co.uk"

    # for basic auth, if access to secure3 via 100007 does not have password, return 100107 instead
    if called_ident[1] == 100007:
        # check user allowed to go to secure page 3
        auth = skicall.environ.get('HTTP_AUTHORIZATION')
        if auth:
            scheme, data = auth.split(" ", 1)
            assert scheme.lower() == 'basic'
            username, password = b64decode(data).decode('UTF-8').split(':', 1)
            if len(username) > 3 and password == "password3":
                # login ok
                skicall.call_data['USERNAME'] = username
                return called_ident
        # login fail, request a login
        return (skicall.project,100107)

    return called_ident


@use_submit_list
def submit_data(skicall):
    """This function is called when a Responder wishes to submit data for processing in some manner
       For two or more submit_list values, the decorator ensures the matching function is called instead"""

    # Show the server error page
    if skicall.submit_list and (skicall.submit_list[0] == 'server_error'):
        raise ServerError(message="This is a deliberate error to show the ServerError page", code=666)
    raise ServerError("submit_list string not recognised")



_HEADER_TEXT = { 2001 : "Project skitest.",
                 9101 : "Widget Modules.",
                 9102 : "Widgets in module ",
                 9103 : "Tests of ",
               100101 : "Login Tests",
               100102 : "Secure 1",
               100104 : "Secure 2",
               100106 : "Secure 3",
               210001 : "Responders",
               300001 : "Validator Modules.",
               300002 : "Basic Validators.",
               300003 : "Allowed Values.",
               410001 : "Sub-project Tests",
               500101 : "UI Tests"
               }

_NAV_BUTTONS = {
                  2001 : [[9001, 'Widgets', False, ''],
                          ['valtests', 'Validators', False, ''],
                          ['responders_list', 'Responders', False, ''],
                          [550, 'Validate Error Page', False, ''],
                          [560, 'Server Error Page', False, ''],
                          ['login', 'Test Login', False, ''],
                          [400001, 'Sub Projects', False, ''],
                          [500001, 'JqueryUI', False, '']],
                  9101 : [['home','Home', False, '']],
                  9102 : [['home','Home', False, ''],['modules','Modules', False, '']],
                  9103 : [['home','Home', False, ''],['modules','Modules', False, '']],
                100101 : [['home','Home', False, '']],
                100102 : [['home','Home', False, ''],['login', 'Test Login', False, '']],
                100104 : [['home','Home', False, ''],['login', 'Test Login', False, '']],
                100106 : [['home','Home', False, ''],['login', 'Test Login', False, '']],
                210001 : [['home','Home', False, '']],
                300001 : [['home','Home', False, '']],
                300002 : [['home','Home', False, ''],['valtests', 'Validators', False, '']],
                300003 : [['home','Home', False, ''],['valtests', 'Validators', False, ''], [300002, 'Basic', False, '']],
                410001 : [['home','Home', False, '']],
                500101 : [['home','Home', False, '']]

                }

def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with page_data,
       it can also return an optional ident_data string to embed into forms."""
    if page_type != "TemplatePage":
        return
    page_num = page_ident[1]
    # Insert header text into the template page
    if page_num in _HEADER_TEXT:
        skicall.page_data['header', 'headpara', 'para_text']  = _HEADER_TEXT[page_num]
    # add further text to the header, if text is given in call_data['headtext']
    if 'headtext' in skicall.call_data:
       skicall.page_data['header', 'headpara', 'para_text'] +=  skicall.call_data['headtext']
    # Insert navigation links into the template page
    if page_num in _NAV_BUTTONS:
        skicall.page_data['navigation', 'navbuttons', 'nav_links'] = _NAV_BUTTONS[page_num][:]
    # append another link in the nav buttons, if a link list is given in call_data['navlink']
    if 'navlink' in skicall.call_data:
        skicall.page_data['navigation', 'navbuttons', 'nav_links'].append(skicall.call_data['navlink'])    
    # Insert a status message into the footer if call_data['status'] is given
    if 'status' in skicall.call_data:
        skicall.page_data['foot','foot_status','footer_text'] = skicall.call_data['status']
    if page_num == 500101:
        # If this is the page of jquery UI tests, add the required javascript
        skicall.page_data['add_jscript'] = """
$( "#date" ).datepicker();
"""
    # set secure1 cookie
    if 'session' in skicall.call_data:
        return skicall.call_data['session']


# create the wsgi application
application = WSGIApplication(project=PROJECT,
                              projectfiles=PROJECTFILES,
                              proj_data={},
                              start_call=start_call,
                              submit_data=submit_data,
                              end_call=end_call,
                              url="/test")



skis_application = skis.makeapp()
application.add_project(skis_application, url='/test/lib')

# add widget sub projects

# import the module where the code for each test widget is found
import widgetprojects

# from this module, obtain and import each further module containing a widget test application

module_tuple = tuple(name for (module_loader, name, ispkg) in pkgutil.iter_modules(widgetprojects.__path__))
for name in module_tuple:
    appmodule = import_module('widgetprojects.' + name)
    widget_application = appmodule.makeapp(PROJECTFILES)
    application.add_project(widget_application, url='/test/'+name)



if __name__ == "__main__":

    # If called as a script, this portion runs the python wsgiref.simple_server
    # and serves the project.

    ###############################################################################
    #
    # you could add the 'skiadmin' sub project
    # which can be used to develop pages for your project
    #
    ############################### THESE LINES ADD SKIADMIN ######################
    #                                                                             #
    #set_debug(True)                                                               #
    #from skipole import skiadmin                                                  #
    #skiadmin_application = skiadmin.makeapp(editedprojname=PROJECT)               #
    #application.add_project(skiadmin_application, url='/test/skiadmin')           #
    #                                                                             #
    ###############################################################################

    # if using the waitress server
    # from waitress import serve

    # or the skilift development server
    from skipole import skilift

    # serve the application, note host 0.0.0.0 rather than
    # 127.0.0.1 - so this will be available externally

    host = "0.0.0.0"
    port = 8000
    print("Serving %s on port %s" % (PROJECT, port))

    # using waitress
    # serve(application, host, port)

    # or skilift
    skilift.development_server(host, port, application)



