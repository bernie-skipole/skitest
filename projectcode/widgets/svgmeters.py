import random

from ... import FailPage, GoTo, ValidateError, ServerError


_NUMBERS = [ n for n in range(5, 95)]

def populate_vertical1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Sets content into vertical1"""
    page_data['vertical1', 'measurement'] = random.choice(_NUMBERS)



def populate_traditional1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Sets content into traditional1"""
    page_data['traditional1', 'measurement'] = random.choice(_NUMBERS)

