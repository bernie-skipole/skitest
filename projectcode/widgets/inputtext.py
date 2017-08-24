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





