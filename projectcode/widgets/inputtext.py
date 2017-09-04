from ... import FailPage, GoTo, ValidateError, ServerError
from .... import skilift

def textinput1_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from textinput1 widget"""
    if ('textinput1_test1','input_text') in call_data:
        page_data['result','para_text'] = call_data['textinput1_test1','input_text']

def textinput2_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from textinput2 widget"""
    if ('textinput2_test1','input_text') in call_data:
        page_data['result','para_text'] = call_data['textinput2_test1','input_text']

def textinput3_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from textinput3 widget"""
    if ('textinput3_test1','input_text') in call_data:
        page_data['result','para_text'] = call_data['textinput3_test1','input_text']

def textinput4_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from textinput4 widget"""
    if ('textinput4_test1','input_text') in call_data:
        page_data['result','para_text'] = call_data['textinput4_test1','input_text']

def password1_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from password1 widget"""
    if ('password1_test1','input_text') in call_data:
        page_data['result','para_text'] = call_data['password1_test1','input_text']


def password2_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from password2 widget"""
    if ('password2_test1','input_text') in call_data:
        page_data['result','para_text'] = call_data['password2_test1','input_text']

def submittextinput1_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from submittextinput1 widget"""
    if ('submittextinput1_test1','input_text') in call_data:
        page_data['result','para_text'] = call_data['submittextinput1_test1','input_text']


def submittextinput3_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from submittextinput3 widget"""
    if ('submittextinput3_test1','input_text') in call_data:
        page_data['result','para_text'] = call_data['submittextinput3_test1','input_text']

def submittextinput3_test2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Displays first paragraph of submittextinput3 widget"""
    page_data['submittextinput3_test1','show_para1'] = True

def submittextinput3_test3(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Hides first paragraph of submittextinput3 widget"""
    page_data['submittextinput3_test1','show_para1'] = False

def submittextinput3_test4(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Displays second paragraph of submittextinput3 widget"""
    page_data['submittextinput3_test1','show_para2'] = True

def submittextinput3_test5(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Hides second paragraph of submittextinput3 widget"""
    page_data['submittextinput3_test1','show_para2'] = False

def submittextinput3_test6(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from submittextinput1 widget and puts it into paragraph of submittextinput3_test1 widget"""
    if ('submittextinput3_test6','input_text') in call_data:
        page_data['submittextinput3_test1','para_text'] = call_data['submittextinput3_test6','input_text']
        page_data['submittextinput3_test1','show_para1'] = True


def twoinputssubmit1_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Takes input from TwoInputsSubmit1 widget"""
    if ('twoinputssubmit1_test1','input_text1') in call_data:
        text1 = call_data['twoinputssubmit1_test1','input_text1']
    else:
        text1 = ''
    if ('twoinputssubmit1_test1','input_text2') in call_data:
        text2 = call_data['twoinputssubmit1_test1','input_text2']
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


