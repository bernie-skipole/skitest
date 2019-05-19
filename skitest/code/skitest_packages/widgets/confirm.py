from skipole import FailPage, GoTo, ValidateError, ServerError

def alertclear1_test1(skicall):
    """Displays alertclear1"""
    skicall.page_data['alertclear1', 'hide'] = False
    skicall.page_data['alertclear1', 'para_text'] = """Text sent from a submit_data function, this refreshes the full page, and sets the alertclear1 widget 'hide' field to False, which therefore should display this message."""

def alertclear1_test2(skicall):
    """Displays alertclear1"""
    skicall.page_data['alertclear1', 'hide'] = False
    skicall.page_data['alertclear1', 'para_text'] = """Text sent from a submit_data function, which returns a JSON page, and sets the alertclear1 widget 'hide' field to False, which therefore should display this message."""


def alertclear1_test3(skicall):
    raise FailPage(message="This raises an error and refreshes the page", widget='alertclear1')

def alertclear1_test4(skicall):
    raise FailPage(message="This raises an error and sends JSON file", widget='alertclear1')


def confirmbox2_test1(skicall):
    """Displays confirmbox2 by HTML"""
    skicall.page_data['confirmbox2', 'hide'] = False
    skicall.page_data['confirmbox2', 'para_text'] = """Text sent from a submit_data function, this refreshes the full page, and sets the confirmbox2 widget 'hide' field to False, which therefore should display this message."""

def confirmbox2_test2(skicall):
    """Displays confirmbox2 by JSON"""
    skicall.page_data['confirmbox2', 'hide'] = False
    skicall.page_data['confirmbox2', 'para_text'] = """Text sent from a submit_data function, this sends a JSON file with the confirmbox2 widget 'hide' field set to False, which therefore should display this message."""
