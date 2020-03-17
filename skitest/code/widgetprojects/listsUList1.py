
from skipole import WSGIApplication, FailPage, GoTo, ValidateError, ServerError

def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    return called_ident


def submit_data(skicall):
    "This function is called when a Responder wishes to submit data for processing in some manner"
    if skicall.submit_list[0] == 'index':
        skicall.page_data['testwidget', 'contents'] = ["""Text in list\nwith a second line""",
                                                       """Text in list item 2"""]
    elif skicall.submit_list[0] == 'test1':
        skicall.page_data['testwidget', 'contents'] = ["""Text in list item 2""",
                                                       """Text in list\nwith a second line"""]
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return

def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='listsUList1',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")



