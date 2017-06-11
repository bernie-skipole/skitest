from ....skilift import FailPage, GoTo, ValidateError, ServerError

def errordiv_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error for errordiv"""
    raise FailPage(message = """This error message set in a Failpage exception by a submit data function.""", displaywidgetname="testerrordiv")

def errordiv_test2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error for errordiv, with no message, errordiv default message should be shown"""
    raise FailPage(displaywidgetname="testerrordiv")

def errordiv_test5(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Clears an error for errordiv"""
    page_data['testerrordiv', 'clear_error'] = True


def errordiv_test6(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Puts received string in resulttext,para_text"""
    if call_data['textinput','input_text']:
        page_data['resulttext','para_text'] = "Text received : %s." % call_data['textinput','input_text']
    else:
        page_data['resulttext','para_text'] = "No text received."


def errorpara_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error for errorpara"""
    raise FailPage(message = """This error message set in a Failpage exception by a submit data function.""", displaywidgetname="testerrorpara")

def errorpara_test2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error for errorpara, with no message, errorpara default message should be shown"""
    raise FailPage(displaywidgetname="testerrorpara")

def errorpara_test5(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Clears an error for errorpara"""
    page_data['testerrorpara', 'clear_error'] = True


def errorpara_test6(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Puts received string in resulttext,para_text"""
    if call_data['textinput','input_text']:
        page_data['resulttext','para_text'] = "Text received : %s." % call_data['textinput','input_text']
    else:
        page_data['resulttext','para_text'] = "No text received."


def errorclear1_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error for errorclear1"""
    raise FailPage(message="Error message sent by Responder", displaywidgetname="testerrorclear1")

def errorclear1_test3(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Displays text for errorclear1"""
    page_data["testerrorclear1", "hide"] = False
    page_data["testerrorclear1", "para_text"] = "This text is sent by responder\nIt is not an error message."





