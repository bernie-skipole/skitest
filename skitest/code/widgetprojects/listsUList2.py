
from skipole import WSGIApplication, FailPage, GoTo, ValidateError, ServerError

def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    return called_ident


def submit_data(skicall):
    "This function is called when a Responder wishes to submit data for processing in some manner"
    if skicall.submit_list[0] == 'index':
        skicall.page_data['testwidget', 'set_html'] = ["""<p class="w3-red">Item 1 in the list</p>""",
                                                       """<p class="w3-blue">Item 2 in the list</p>"""]
    elif skicall.submit_list[0] == 'test1':
        skicall.page_data['testwidget', 'set_html'] = ["""<p class="w3-green">Item 1 in the list</p>""",
                                                       """<p class="w3-yellow">Item 2 in the list</p>"""]
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return

def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='listsUList2',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")



