from ....skilift import FailPage, GoTo, ValidateError, ServerError

def test_blue(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Tests submitcss by returning a css style makeblue"""
    style = { '.makeblue': [['background-color', 'blue'], ['color', 'white']] }
    return style
