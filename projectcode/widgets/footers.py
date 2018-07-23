from ... import FailPage, GoTo, ValidateError, ServerError
from .... import skilift

def set_style(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    "Sets the style on the simplefooter"
    page_data['testftr', 'widget_style'] = "color:green;background-color:yellow"
    page_data['testftr', 'clear_error'] = True



def set_text(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    "Sets the text on the simplefooter"
    page_data['testftr', 'footer_text'] = "New text on this SimpleFooter has been set by JSON call"
    page_data['testftr', 'clear_error'] = True


def set_error(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    "Raises an error with a message on the simplefooter"
    raise FailPage(message="An error message is displayed here", widget='testftr')
