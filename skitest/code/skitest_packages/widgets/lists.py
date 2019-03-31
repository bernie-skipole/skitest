from skipole import FailPage, GoTo, ValidateError, ServerError


def populate_ulist1(skicall):
    """Sets content into ulist1"""
    skicall.page_data['ulist1', 'contents'] = ["First element text string",
                                       "Text string with <p>tags</p> to show they are escaped",
                                       "Text string with \nnewline to show br inserted",
                                       "Fourth element text string"]


def set_by_json(skicall):
    """Sets content into ulist1"""
    skicall.page_data['ulist1', 'contents'] = ["First element text string - set by JSON",
                                       "Text string with \nnewline to show br inserted",
                                       "Text string with <p>tags</p> to show they are escaped",
                                       "Fourth element text string - set by JSON",
                                       "Extra fifth element to show JSON can set a new number of elements"]

