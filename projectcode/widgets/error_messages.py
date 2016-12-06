from ....skilift import FailPage, GoTo, ValidateError, ServerError

def errordiv_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error for errordiv"""
    raise FailPage(message = """This error message set in a Failpage exception by a submit data function.""", displaywidgetname="testerrordiv")

def errordiv_test2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Raises an error for errordiv, with mo message, errordiv default message should be shown"""
    raise FailPage(displaywidgetname="testerrordiv")
