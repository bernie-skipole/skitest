
from skipole import WSGIApplication, FailPage, GoTo, ValidateError, ServerError

def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    return called_ident


def submit_data(skicall):
    "This function is called when a Responder wishes to submit data for processing in some manner"

    # setting up the drop down
    # Field name : nav_links

    # A list of lists, each inner list describing a link, the name of this field is used in the widgfield for any data returned in the get field
    # For each navigation link, the inner list elements are:
    # 0 : The url, label or ident of the target page of the link
    # 1 : The displayed text of the link
    # 2 : If True, ident is appended to link even if there is no get field
    # 3 : The get field data to send with the link

    if skicall.submit_list[0] == 'index':
        skicall.page_data['dropdownbutton1', 'nav_links'] = [[3, 'test1', True, ''],[4, 'test2', True, ''],[5, 'test3', True, '']]
    elif skicall.submit_list[0] == 'test1':
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
    skicall.page_data['result', 'para_text'] = "Test1 has been pressed"
    

def _test2(skicall):
    """Test 2"""
    skicall.page_data['result', 'para_text'] = "Test2 has been pressed"


def _test3(skicall):
    """Test 3"""
    skicall.page_data['result', 'para_text'] = "Test3 has been pressed"


def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='headersDropDownButton1',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")
