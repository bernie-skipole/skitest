from ... import FailPage, GoTo, ValidateError, ServerError

def check1(skicall):
    """Tests CheckBox1 when submitted in a form"""
    if skicall.call_data['check1','checkbox'] == 'check1':
        skicall.page_data['check1result', 'para_text'] = "Form submission result: The checkbox is TICKED."
        skicall.page_data['check1', 'checked'] = True
    else:
       skicall.page_data['check1result', 'para_text'] = "Form submission result: The checkbox is NOT TICKED."
       skicall.page_data['check1', 'checked'] = False


def check2(skicall):
    """Raises an error in CheckBox1"""
    raise FailPage(message="Test error raised", widget='check1')


def check5(skicall):
    """Raises an error in CheckBox1 by JSON"""
    raise FailPage(message="Test error raised", widget='check1')


def check10(skicall):
    """Tests CheckBox2 when submitted in a form"""
    if skicall.call_data['check10','checkbox'] == 'check10':
        skicall.page_data['check10result', 'para_text'] = "Form submission result: The checkbox is TICKED."
        skicall.page_data['check10', 'checked'] = True
    else:
       skicall.page_data['check10result', 'para_text'] = "Form submission result: The checkbox is NOT TICKED."
       skicall.page_data['check10', 'checked'] = False



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


