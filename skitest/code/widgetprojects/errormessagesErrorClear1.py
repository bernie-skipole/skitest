

from skipole import WSGIApplication, FailPage, GoTo, ValidateError, ServerError


def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    return called_ident


def submit_data(skicall):
    "This function is called when a Responder wishes to submit data for processing in some manner"
    if skicall.submit_list[0] == 'errorclear1_test1':
        _errorclear1_test1(skicall)
    elif skicall.submit_list[0] == 'errorclear1_test3':
        _errorclear1_test3(skicall)
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return


def _errorclear1_test1(skicall):
    """Raises an error for errorclear1"""
    raise FailPage(message="Error message sent by Responder", widget="testerrorclear1")

def _errorclear1_test3(skicall):
    """Displays text for errorclear1"""
    skicall.page_data["testerrorclear1", "hide"] = False
    skicall.page_data["testerrorclear1", "para_text"] = "This text is sent by responder\nIt is not an error message."

def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='errormessagesErrorClear1',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")


