
from collections import OrderedDict

from skipole import FailPage, GoTo, ValidateError, ServerError


def textinput1_test1(skicall):
    """Takes input from textinput1 widget"""
    if ('textinput1_test1','input_text') in skicall.call_data:
        skicall.page_data['result','para_text'] = skicall.call_data['textinput1_test1','input_text']

def textinput2_test1(skicall):
    """Takes input from textinput2 widget"""
    if ('textinput2_test1','input_text') in skicall.call_data:
        skicall.page_data['result','para_text'] = skicall.call_data['textinput2_test1','input_text']

def textinput3_test1(skicall):
    """Takes input from textinput3 widget"""
    if ('textinput3_test1','input_text') in skicall.call_data:
        skicall.page_data['result','para_text'] = skicall.call_data['textinput3_test1','input_text']

def textinput4_test1(skicall):
    """Takes input from textinput4 widget"""
    if ('textinput4_test1','input_text') in skicall.call_data:
        skicall.page_data['result','para_text'] = skicall.call_data['textinput4_test1','input_text']

def password1_test1(skicall):
    """Takes input from password1 widget"""
    if ('password1_test1','input_text') in skicall.call_data:
        skicall.page_data['result','para_text'] = skicall.call_data['password1_test1','input_text']


def password2_test1(skicall):
    """Takes input from password2 widget"""
    if ('password2_test1','input_text') in skicall.call_data:
        skicall.page_data['result','para_text'] = skicall.call_data['password2_test1','input_text']

def submittextinput1_test1(skicall):
    """Takes input from submittextinput1 widget"""
    if ('submittextinput1_test1','input_text') in skicall.call_data:
        skicall.page_data['result','para_text'] = skicall.call_data['submittextinput1_test1','input_text']


def submittextinput3_test1(skicall):
    """Takes input from submittextinput3 widget"""
    if ('submittextinput3_test1','input_text') in skicall.call_data:
        skicall.page_data['result','para_text'] = skicall.call_data['submittextinput3_test1','input_text']

def submittextinput3_test2(skicall):
    """Displays first paragraph of submittextinput3 widget"""
    skicall.page_data['submittextinput3_test1','show_para1'] = True

def submittextinput3_test3(skicall):
    """Hides first paragraph of submittextinput3 widget"""
    skicall.page_data['submittextinput3_test1','show_para1'] = False

def submittextinput3_test4(skicall):
    """Displays second paragraph of submittextinput3 widget"""
    skicall.page_data['submittextinput3_test1','show_para2'] = True

def submittextinput3_test5(skicall):
    """Hides second paragraph of submittextinput3 widget"""
    skicall.page_data['submittextinput3_test1','show_para2'] = False

def submittextinput3_test6(skicall):
    """Takes input from submittextinput1 widget and puts it into paragraph of submittextinput3_test1 widget"""
    if ('submittextinput3_test6','input_text') in skicall.call_data:
        skicall.page_data['submittextinput3_test1','para_text'] = skicall.call_data['submittextinput3_test6','input_text']
        skicall.page_data['submittextinput3_test1','show_para1'] = True


def twoinputssubmit1_test1(skicall):
    """Takes input from TwoInputsSubmit1 widget"""
    if ('twoinputssubmit1_test1','input_text1') in skicall.call_data:
        text1 = skicall.call_data['twoinputssubmit1_test1','input_text1']
    else:
        text1 = ''
    if ('twoinputssubmit1_test1','input_text2') in skicall.call_data:
        text2 = skicall.call_data['twoinputssubmit1_test1','input_text2']
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



def twoinputssubmit1_test2(skicall):
    """Sets flags in input fields"""
    skicall.page_data['twoinputssubmit1_test1', 'set_input_accepted1'] = True
    skicall.page_data['twoinputssubmit1_test1', 'set_input_errored2'] = True


def fill_submitdict1(skicall):
    """Fills in the submitdict1 page"""
    skicall.page_data['submitdict1_test1', 'input_dict'] = OrderedDict([('one',''), ('two',''), ('three','')])


def submitdict1_test1(skicall):
    """Takes input from SubmitDict1 widget"""
    if ('submitdict1_test1','input_dict') in skicall.call_data:
        skicall.page_data['result','para_text'] = str(skicall.call_data['submitdict1_test1','input_dict'])
    else:
        skicall.page_data['result','para_text'] = "Nothing received"



