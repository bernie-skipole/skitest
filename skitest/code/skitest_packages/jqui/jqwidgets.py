from skipole import FailPage, GoTo, ValidateError, ServerError


def set_date(skicall):
    """Sets date given in call_data into the showdate paragraph"""
    if ('date','input_text') in skicall.call_data:
        skicall.page_data['showdate', 'para_text'] = "The date set is " + skicall.call_data['date','input_text']



