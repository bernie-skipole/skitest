from ... import FailPage, GoTo, ValidateError, ServerError
from .... import skilift

def populate_ulist1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Sets content into ulist1"""
    page_data['ulist1', 'contents'] = ["First element text string",
                                       "Text string with <p>tags</p> to show they are escaped",
                                       "Text string with \nnewline to show br inserted",
                                       "Fourth element text string"]


def set_by_json(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Sets content into ulist1"""
    page_data['ulist1', 'contents'] = ["First element text string - set by JSON",
                                       "Text string with \nnewline to show br inserted",
                                       "Text string with <p>tags</p> to show they are escaped",
                                       "Fourth element text string - set by JSON",
                                       "Extra fifth element to show JSON can set a new number of elements"]

