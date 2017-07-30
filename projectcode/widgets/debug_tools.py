from ... import FailPage, GoTo, ValidateError, ServerError
from .... import skilift

def toggle_debug_mode(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Toggles the debug mode"""
    if skilift.get_debug():
        skilift.set_debug(False)
    else:
        skilift.set_debug(True)



