

from ... import FailPage, GoTo, ValidateError, ServerError



def namepasswd1_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from NamePasswd1 widget"""
    if ('namepasswd1_test1','input_text1') in call_data:
        text1 = call_data['namepasswd1_test1','input_text1']
    else:
        text1 = ''
    if ('namepasswd1_test1','input_text2') in call_data:
        text2 = call_data['namepasswd1_test1','input_text2']
    else:
        text2 = ''
    if text1 and text2:
        page_data['result','para_text'] = text1 + " , " + text2
    elif text1:
        page_data['result','para_text'] = text1
    elif text2:
        page_data['result','para_text'] = text2
    else:
        page_data['result','para_text'] = "Nothing received"



def namepasswd1_test2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Sets flags in input fields"""
    page_data['namepasswd1_test1', 'set_input_accepted1'] = True
    page_data['namepasswd1_test1', 'set_input_errored2'] = True




