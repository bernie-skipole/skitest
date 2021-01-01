
from skipole import WSGIApplication, FailPage, GoTo, ValidateError, ServerError


def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    return called_ident


def submit_data(skicall):
    "This function is called when a Responder wishes to submit data for processing in some manner"
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return


def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='debugtoolsShowEnviron',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")

if __name__ == "__main__":

    import os

    PROJECTFILES = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    PROJECT='debugtoolsShowEnviron'

    application = makeapp(PROJECTFILES)

    from skipole import skiadmin, skis, skilift, set_debug

    set_debug(True)

    skis_application = skis.makeapp()
    application.add_project(skis_application, url='/lib')

    skiadmin_application = skiadmin.makeapp(editedprojname=PROJECT) 
    application.add_project(skiadmin_application, url='/skiadmin')

    from skipole import skilift

    # serve the application

    host = "127.0.0.1"
    port = 8000
    print("Serving %s on port %s" % (PROJECT, port))

    skilift.development_server(host, port, application)



