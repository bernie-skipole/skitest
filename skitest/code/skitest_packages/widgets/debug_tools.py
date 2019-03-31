from skipole import FailPage, GoTo, ValidateError, ServerError
from skipole import skilift


def toggle_debug_mode(skicall):
    """Toggles the debug mode"""
    if skilift.get_debug():
        skilift.set_debug(False)
    else:
        skilift.set_debug(True)



