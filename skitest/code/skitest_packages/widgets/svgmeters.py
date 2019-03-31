import random

from ... import FailPage, GoTo, ValidateError, ServerError


_NUMBERS = [ n for n in range(5, 95)]

def populate_vertical1(skicall):
    """Sets content into vertical1"""
    skicall.page_data['vertical1', 'measurement'] = random.choice(_NUMBERS)



def populate_traditional1(skicall):
    """Sets content into traditional1"""
    skicall.page_data['traditional1', 'measurement'] = random.choice(_NUMBERS)

