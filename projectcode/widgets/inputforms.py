from ... import FailPage, GoTo, ValidateError, ServerError

def hiddenfield_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """reades value of hiddenfield"""
    value = call_data['hf_test1', 'hidden_field']
    page_data['test1result','para_text'] = "The value of the hidden field is: " + value





