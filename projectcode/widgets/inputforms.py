from ... import FailPage, GoTo, ValidateError, ServerError

def hiddenfield_test1(skicall):
    """reades value of hiddenfield"""
    value = skicall.call_data['hf_test1', 'hidden_field']
    skicall.page_data['test1result','para_text'] = "The value of the hidden field is: " + value





