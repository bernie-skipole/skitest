def test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Allowed values only submitted"""
    if call_data['test1','input_text']:
        page_data['result_test1', 'para_text'] = call_data['test1','input_text']

