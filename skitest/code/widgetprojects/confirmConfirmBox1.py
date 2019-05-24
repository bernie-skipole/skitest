

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
    elif skicall.submit_list[0] == 'test3':
        _test3(skicall)
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return



def _test1(skicall):
    """Displays confirmbox1 by HTML"""
    skicall.page_data['confirmbox1', 'hide'] = False
    skicall.page_data['confirmbox1', 'para_text'] = """Text sent from a submit_data function, this refreshes the full page, and sets the confirmbox1 widget 'hide' field to False, which therefore should display this message."""

def _test2(skicall):
    """Displays confirmbox1 by JSON"""
    skicall.page_data['confirmbox1', 'hide'] = False
    skicall.page_data['confirmbox1', 'para_text'] = """Text sent from a submit_data function, this sends a JSON file with the confirmbox1 widget 'hide' field set to False, which therefore should display this message."""

def _test3(skicall):
    """Hide confirmbox1"""
    skicall.page_data['confirmbox1', 'hide'] = True


def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='confirmConfirmBox1',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")

