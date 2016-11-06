from ....skilift import FailPage, GoTo, ValidateError, ServerError

def check1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Tests CheckBox1 when submitted in a form"""
    if call_data['check1','checkbox'] == 'check1':
        page_data['check1result', 'para_text'] = "Form submission result: The checkbox is TICKED."
        page_data['check1', 'checked'] = True
    else:
       page_data['check1result', 'para_text'] = "Form submission result: The checkbox is NOT TICKED."
       page_data['check1', 'checked'] = False


def check2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error in CheckBox1"""
    raise FailPage(message="Test error raised", displaywidgetname='check1')


def check5(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error in CheckBox1 by JSON"""
    raise FailPage(message="Test error raised", displaywidgetname='check1')


def check10(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Tests CheckBox2 when submitted in a form"""
    if call_data['check10','checkbox'] == 'check10':
        page_data['check10result', 'para_text'] = "Form submission result: The checkbox is TICKED."
        page_data['check10', 'checked'] = True
    else:
       page_data['check10result', 'para_text'] = "Form submission result: The checkbox is NOT TICKED."
       page_data['check10', 'checked'] = False



def check20(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Tests Checkedtext when submitted in a form"""
    submitted_text = call_data['check20','input_text']
    if call_data['check20','checkbox'] == 'check20':
        if submitted_text:
            page_data['check20result', 'para_text'] = "Form submission result: The checkbox is TICKED. Text: %s" % (submitted_text,)
        else:
            page_data['check20result', 'para_text'] = "Form submission result: The checkbox is TICKED."
        page_data['check20', 'checked'] = True
    else:
        if submitted_text:
            page_data['check20result', 'para_text'] = "Form submission result: The checkbox is NOT TICKED. Text: %s" % (submitted_text,)
        else:
           page_data['check20result', 'para_text'] = "Form submission result: The checkbox is NOT TICKED."
        page_data['check20', 'checked'] = False


