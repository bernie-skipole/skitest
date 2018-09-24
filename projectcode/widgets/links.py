from ... import FailPage, GoTo, ValidateError, ServerError

def table1button(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Populates Table1_Button test page"""
    # col 0 is the text string to place in the first column,
    # col 1 is the get field contents of the button link
    page_data['table1button', 'contents'] = [["Row 0 text", "test1"], ["Row 1 text", "test2"]]
    page_data['table1button2', 'contents'] = [["Row 0 text", "test1"], ["Row 1 text", "test2"]]


def table1button_jsontest(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Send JSON page after table button pressed"""
    if call_data['table1button', 'contents'] == 'test1':
        page_data['paratest','para_text'] = "First row button pressed"
    if call_data['table1button', 'contents'] == 'test2':
        page_data['paratest','para_text'] = "Second row button pressed"

def table1button_htmltest(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Renew HML page after table button pressed"""
    if call_data['table1button2', 'contents'] == 'test1':
        page_data['paratest','para_text'] = "First row button pressed"
    if call_data['table1button2', 'contents'] == 'test2':
        page_data['paratest','para_text'] = "Second row button pressed"


def messagebutton(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    "Set text into Messagebox"
    page_data['messagebutton', 'para_text'] = "This text placed by JSON file"
