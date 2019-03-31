from skipole import FailPage, GoTo, ValidateError, ServerError

def errordiv_test1(skicall):
    """Raises an error for errordiv"""
    raise FailPage(message = """This error message set in a Failpage exception by a submit data function.""", widget="testerrordiv")

def errordiv_test2(skicall):
    """Raises an error for errordiv, with no message, errordiv default message should be shown"""
    raise FailPage(widget="testerrordiv")

def errordiv_test5(skicall):
    """Clears an error for errordiv"""
    skicall.page_data['testerrordiv', 'clear_error'] = True


def errordiv_test6(skicall):
    """Puts received string in resulttext,para_text"""
    if skicall.call_data['textinput','input_text']:
        skicall.page_data['resulttext','para_text'] = "Text received : %s." % skicall.call_data['textinput','input_text']
    else:
        skicall.page_data['resulttext','para_text'] = "No text received."


def errorpara_test1(skicall):
    """Raises an error for errorpara"""
    raise FailPage(message = """This error message set in a Failpage exception by a submit data function.""", widget="testerrorpara")

def errorpara_test2(skicall):
    """Raises an error for errorpara, with no message, errorpara default message should be shown"""
    raise FailPage(widget="testerrorpara")

def errorpara_test5(skicall):
    """Clears an error for errorpara"""
    skicall.page_data['testerrorpara', 'clear_error'] = True


def errorpara_test6(skicall):
    """Puts received string in resulttext,para_text"""
    if skicall.call_data['textinput','input_text']:
        skicall.page_data['resulttext','para_text'] = "Text received : %s." % skicall.call_data['textinput','input_text']
    else:
        skicall.page_data['resulttext','para_text'] = "No text received."


def errorclear1_test1(skicall):
    """Raises an error for errorclear1"""
    raise FailPage(message="Error message sent by Responder", widget="testerrorclear1")

def errorclear1_test3(skicall):
    """Displays text for errorclear1"""
    skicall.page_data["testerrorclear1", "hide"] = False
    skicall.page_data["testerrorclear1", "para_text"] = "This text is sent by responder\nIt is not an error message."

def errorclear2_test1(skicall):
    """Raises an error for errorclear2"""
    raise FailPage(message="Error message sent by Responder and HTML page refresh", widget="testerrorclear2")

def errorclear2_test2(skicall):
    """Raises an error for errorclear2"""
    raise FailPage(message="Error message sent by Responder via JSON file", widget="testerrorclear2")

def errorclear2_test3(skicall):
    """Raises default error message for errorclear2"""
    raise FailPage(widget="testerrorclear2")





