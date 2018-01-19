from ... import FailPage, GoTo, ValidateError, ServerError
from .... import skilift

def populate_chart1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Sets content into chart1"""
    page_data['chart1', 'values'] = [100,50,0,-50,-100, -80, -60, -40, -20, 0, 20, 40, 60, 80]


def set_by_json(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Sets content into chart1"""
    page_data['chart1', 'values'] = [-100,-50,0,50,100, 80, 60, 40, 20, 0, -20, -40, -60, -80]

