
from skipole import WSGIApplication, FailPage, GoTo, ValidateError, ServerError

def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    return called_ident


def submit_data(skicall):
    "This function is called when a Responder wishes to submit data for processing in some manner"
    if skicall.submit_list[0] == 'test1':
        _test1(skicall)
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return


def _test1(skicall):
    """Tests Checkedtext when submitted in a form"""
    submitted_text = skicall.call_data['check','input_text']
    if skicall.call_data['check','checkbox'] == 'check':
        if submitted_text:
            skicall.page_data['checkresult', 'para_text'] = "Form submission result: The checkbox is TICKED. Text: %s" % (submitted_text,)
        else:
            skicall.page_data['checkresult', 'para_text'] = "Form submission result: The checkbox is TICKED."
        skicall.page_data['check', 'checked'] = True
    else:
        if submitted_text:
            skicall.page_data['checkresult', 'para_text'] = "Form submission result: The checkbox is NOT TICKED. Text: %s" % (submitted_text,)
        else:
           skicall.page_data['checkresult', 'para_text'] = "Form submission result: The checkbox is NOT TICKED."
        skicall.page_data['check', 'checked'] = False


def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='checkboxCheckedText',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")

