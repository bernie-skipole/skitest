

from skipole import FailPage, GoTo, ValidateError, ServerError



def namepasswd1_test1(skicall):
    """Takes input from NamePasswd1 widget"""
    if ('namepasswd1_test1','input_text1') in skicall.call_data:
        text1 = skicall.call_data['namepasswd1_test1','input_text1']
    else:
        text1 = ''
    if ('namepasswd1_test1','input_text2') in skicall.call_data:
        text2 = skicall.call_data['namepasswd1_test1','input_text2']
    else:
        text2 = ''
    if text1 and text2:
        skicall.page_data['result','para_text'] = text1 + " , " + text2
    elif text1:
        skicall.page_data['result','para_text'] = text1
    elif text2:
        skicall.page_data['result','para_text'] = text2
    else:
        skicall.page_data['result','para_text'] = "Nothing received"



def namepasswd1_test2(skicall):
    """Sets flags in input fields"""
    skicall.page_data['namepasswd1_test1', 'set_input_accepted1'] = True
    skicall.page_data['namepasswd1_test1', 'set_input_errored2'] = True


def namepasswd1_test3(skicall):
    """clears errors"""
    skicall.page_data['namepasswd1_test1', 'clear_error'] = True




