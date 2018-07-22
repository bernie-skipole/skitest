from ... import FailPage, GoTo, ValidateError, ServerError
from .... import skilift

def set_style(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    "Sets the style on the simplefooter"
    page_data['testftr', 'widget_style'] = "color:green;background-color:yellow"
    page_data['testftr', 'clear_error'] = True

