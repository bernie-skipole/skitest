from ....skilift import FailPage, GoTo, ValidateError, ServerError

def test_blue(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Tests submitcss by returning a css style makeblue, white text on a blue background"""
    return { '.makeblue': [['background-color', 'blue'],
                           ['color', 'white'],
                           ['margin', '10px'],
                           ['padding', '10px']
                           ] }


def test_invblue(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Tests submitcss by returning a css style makeblue, blue text on a white background"""
    return { '.makeblue': [['background-color', 'white'],
                           ['color', 'blue'],
                           ['margin', '10px'],
                           ['padding', '10px']
                           ] }
