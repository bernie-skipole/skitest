from skipole import FailPage, GoTo, ValidateError, ServerError




def check20(skicall):
    """Tests Checkedtext when submitted in a form"""
    submitted_text = skicall.call_data['check20','input_text']
    if skicall.call_data['check20','checkbox'] == 'check20':
        if submitted_text:
            skicall.page_data['check20result', 'para_text'] = "Form submission result: The checkbox is TICKED. Text: %s" % (submitted_text,)
        else:
            skicall.page_data['check20result', 'para_text'] = "Form submission result: The checkbox is TICKED."
        skicall.page_data['check20', 'checked'] = True
    else:
        if submitted_text:
            skicall.page_data['check20result', 'para_text'] = "Form submission result: The checkbox is NOT TICKED. Text: %s" % (submitted_text,)
        else:
           skicall.page_data['check20result', 'para_text'] = "Form submission result: The checkbox is NOT TICKED."
        skicall.page_data['check20', 'checked'] = False


