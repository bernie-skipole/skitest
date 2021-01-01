

from skipole import WSGIApplication, FailPage, GoTo, ValidateError, ServerError

def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    return called_ident


def submit_data(skicall):
    "This function is called when a Responder wishes to submit data for processing in some manner"
    if skicall.submit_list[0] == 'test1':
        _test1(skicall)
    elif skicall.submit_list[0] == 'test2':
        _test2(skicall)
    elif skicall.submit_list[0] == 'test5':
        _test2(skicall)
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return


def _test1(skicall):
    """Tests CheckBox1 when submitted in a form"""
    if skicall.call_data['check1','checkbox'] == 'check1':
        skicall.page_data['check1result', 'para_text'] = "Form submission result: The checkbox is TICKED."
        skicall.page_data['check1', 'checked'] = True
    else:
       skicall.page_data['check1result', 'para_text'] = "Form submission result: The checkbox is NOT TICKED."
       skicall.page_data['check1', 'checked'] = False


def _test2(skicall):
    """Raises an error in CheckBox1"""
    raise FailPage(message="Test error raised", widget='check1')



def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='checkboxCheckBox1',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")

if __name__ == "__main__":

    import os

    PROJECTFILES = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    PROJECT='checkboxCheckBox1'

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


