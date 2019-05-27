

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
    elif skicall.submit_list[0] == 'test4':
        _test4(skicall)
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return


def _test1(skicall):
    """Displays alertclear1"""
    skicall.page_data['alertclear1', 'hide'] = False
    skicall.page_data['alertclear1', 'para_text'] = """Text sent from a submit_data function, this refreshes the full page, and sets the alertclear1 widget 'hide' field to False, which therefore should display this message."""

def _test2(skicall):
    """Displays alertclear1"""
    skicall.page_data['alertclear1', 'hide'] = False
    skicall.page_data['alertclear1', 'para_text'] = """Text sent from a submit_data function, which returns a JSON page, and sets the alertclear1 widget 'hide' field to False, which therefore should display this message."""


def _test3(skicall):
    raise FailPage(message="This raises an error and refreshes the page", widget='alertclear1')


def _test4(skicall):
    raise FailPage(message="This raises an error and sends JSON file", widget='alertclear1')


def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='confirmAlertClear1',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")





