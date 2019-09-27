
from skipole import WSGIApplication, FailPage, GoTo, ValidateError, ServerError

def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    return called_ident


def submit_data(skicall):
    "This function is called when a Responder wishes to submit data for processing in some manner"
    if skicall.submit_list[0] == 'index':
        _options(skicall)
    elif skicall.submit_list[0] == 'test1':
        _test1(skicall)
    elif skicall.submit_list[0] == 'test2':
        raise FailPage("This error is shown in the DropDown1 error paragraph")
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return


def _options(skicall):
    """Fills dropdown"""
    skicall.page_data["dropdown1","option_list"] = ["one","two","three"]
    skicall.page_data["dropdown1","selectvalue"] = "one"


def _test1(skicall):
    """Test 1"""
    _options(skicall)
    selected = skicall.call_data["dropdown1","selectvalue"]
    if selected and (selected in skicall.page_data["dropdown1","option_list"]):
        skicall.page_data["dropdown1","selectvalue"] = selected
        skicall.page_data["result","para_text"] = "The option selected is " + selected


def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='dropdownDropDown1',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call)

