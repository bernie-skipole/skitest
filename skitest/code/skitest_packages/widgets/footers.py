from ... import FailPage, GoTo, ValidateError, ServerError
from .... import skilift

def set_style(skicall):
    "Sets the style on the simplefooter"
    skicall.page_data['testftr', 'widget_style'] = "color:green;background-color:yellow"
    skicall.page_data['testftr', 'clear_error'] = True



def set_text(skicall):
    "Sets the text on the simplefooter"
    skicall.page_data['testftr', 'footer_text'] = "New text on this SimpleFooter has been set by JSON call"
    skicall.page_data['testftr', 'clear_error'] = True


def set_error(skicall):
    "Raises an error with a message on the simplefooter"
    raise FailPage(message="An error message is displayed here", widget='testftr')
