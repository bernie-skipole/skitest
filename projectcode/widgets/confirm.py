from ... import FailPage, GoTo, ValidateError, ServerError

def alertclear1_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Displays alertclear1"""
    page_data['alertclear1', 'hide'] = False
    page_data['alertclear1', 'para_text'] = """Text sent from a submit_data function, this refreshes the full page, and sets the alertclear1 widget 'hide' field to False, which therefore should display this message."""

def alertclear1_test2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Displays alertclear1"""
    page_data['alertclear1', 'hide'] = False
    page_data['alertclear1', 'para_text'] = """Text sent from a submit_data function, which returns a JSON page, and sets the alertclear1 widget 'hide' field to False, which therefore should display this message."""


def alertclear1_test3(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    raise FailPage(message="This raises an error and refreshes the page", widget='alertclear1')

def alertclear1_test4(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    raise FailPage(message="This raises an error and sends JSON file", widget='alertclear1')


def confirmbox1_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Displays confirmbox1 by HTML"""
    page_data['confirmbox1', 'hide'] = False
    page_data['confirmbox1', 'para_text'] = """Text sent from a submit_data function, this refreshes the full page, and sets the confirmbox1 widget 'hide' field to False, which therefore should display this message."""

def confirmbox1_test2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Displays confirmbox1 by JSON"""
    page_data['confirmbox1', 'hide'] = False
    page_data['confirmbox1', 'para_text'] = """Text sent from a submit_data function, this sends a JSON file with the confirmbox1 widget 'hide' field set to False, which therefore should display this message."""

def confirmbox1_test3(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Hide confirmbox1 with json call"""
    page_data['confirmbox1', 'hide'] = True

def confirmbox1_test4(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Hide confirmbox1 with html call"""
    page_data['confirmbox1', 'hide'] = True

def confirmbox2_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Displays confirmbox2 by HTML"""
    page_data['confirmbox2', 'hide'] = False
    page_data['confirmbox2', 'para_text'] = """Text sent from a submit_data function, this refreshes the full page, and sets the confirmbox2 widget 'hide' field to False, which therefore should display this message."""

def confirmbox2_test2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Displays confirmbox2 by JSON"""
    page_data['confirmbox2', 'hide'] = False
    page_data['confirmbox2', 'para_text'] = """Text sent from a submit_data function, this sends a JSON file with the confirmbox2 widget 'hide' field set to False, which therefore should display this message."""
