from ... import FailPage, GoTo, ValidateError, ServerError
from .... import skilift

def set_date(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Sets date given in call_data into the showdate paragraph"""
    if ('date','input_text') in call_data:
        page_data['showdate', 'para_text'] = "The date set is " + call_data['date','input_text']



