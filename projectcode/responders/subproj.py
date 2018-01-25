from ... import FailPage, GoTo, ValidateError, ServerError

def goto_test3(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Tests GoTo can call a labelled page in a sub project"""
    raise GoTo(target = 'lib,test1')


