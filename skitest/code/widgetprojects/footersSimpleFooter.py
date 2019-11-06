

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
    """Test 1"""
    skicall.page_data['simplefooter', 'footer_text'] = "New text set by JSON call"

def _test2(skicall):
    raise FailPage("This is an error message set on the footer")

def _test3(skicall):
    """Test 3"""
    skicall.page_data['simplefooter', 'clear_error'] = True


def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='footersSimpleFooter',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")
