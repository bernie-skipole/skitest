from skipole import FailPage, GoTo, ValidateError, ServerError


def confirmbox2_test1(skicall):
    """Displays confirmbox2 by HTML"""
    skicall.page_data['confirmbox2', 'hide'] = False
    skicall.page_data['confirmbox2', 'para_text'] = """Text sent from a submit_data function, this refreshes the full page, and sets the confirmbox2 widget 'hide' field to False, which therefore should display this message."""

def confirmbox2_test2(skicall):
    """Displays confirmbox2 by JSON"""
    skicall.page_data['confirmbox2', 'hide'] = False
    skicall.page_data['confirmbox2', 'para_text'] = """Text sent from a submit_data function, this sends a JSON file with the confirmbox2 widget 'hide' field set to False, which therefore should display this message."""
