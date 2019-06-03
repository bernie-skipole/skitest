

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
        _test5(skicall)
    elif skicall.submit_list[0] == 'test6':
        _test6(skicall)
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return


def _test1(skicall):
    """Raises an error for errorpara"""
    raise FailPage(message = """This error message set in a Failpage exception by a submit data function.""", widget="testerrorpara")

def _test2(skicall):
    """Raises an error for errorpara, with no message, errorpara default message should be shown"""
    raise FailPage(widget="testerrorpara")

def _test5(skicall):
    """Clears an error for errorpara"""
    skicall.page_data['testerrorpara', 'clear_error'] = True


def _test6(skicall):
    """Puts received string in resulttext,para_text"""
    if skicall.call_data['textinput','input_text']:
        skicall.page_data['resulttext','para_text'] = "Text received : %s." % skicall.call_data['textinput','input_text']
    else:
        skicall.page_data['resulttext','para_text'] = "No text received."


def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='errormessagesErrorPara',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")

