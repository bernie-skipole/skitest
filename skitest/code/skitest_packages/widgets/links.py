from skipole import FailPage, GoTo, ValidateError, ServerError

def table1button(skicall):
    """Populates Table1_Button test page"""
    # col 0 is the text string to place in the first column,
    # col 1 is the get field contents of the button link
    skicall.page_data['table1button', 'contents'] = [["Row 0 text", "test1"], ["Row 1 text", "test2"]]
    skicall.page_data['table1button2', 'contents'] = [["Row 0 text", "test1"], ["Row 1 text", "test2"]]


def table1button_jsontest(skicall):
    """Send JSON page after table button pressed"""
    if skicall.call_data['table1button', 'contents'] == 'test1':
        skicall.page_data['paratest','para_text'] = "First row button pressed"
    if skicall.call_data['table1button', 'contents'] == 'test2':
        skicall.page_data['paratest','para_text'] = "Second row button pressed"

def table1button_htmltest(skicall):
    """Renew HML page after table button pressed"""
    if skicall.call_data['table1button2', 'contents'] == 'test1':
        skicall.page_data['paratest','para_text'] = "First row button pressed"
    if skicall.call_data['table1button2', 'contents'] == 'test2':
        skicall.page_data['paratest','para_text'] = "Second row button pressed"


def messagebutton(skicall):
    "Set text into Messagebox"
    skicall.page_data['messagebutton', 'para_text'] = "This text placed by JSON file"
