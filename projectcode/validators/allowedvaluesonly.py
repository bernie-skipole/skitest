def test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Allowed values only submitted"""
    if call_data['test1','input_text']:
        page_data['result_test1', 'para_text'] = call_data['test1','input_text']


def test2(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Allowed values only submitted"""
    if call_data['test2','input_text']:
        page_data['result_test2', 'para_text'] = call_data['test2','input_text']


def test2fail(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Failed test, show red border"""
    page_data['test2', 'set_input_errored'] = True


def test3(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Allowed values only submitted"""
    if call_data['test3','input_text']:
        page_data['result_test3', 'para_text'] = call_data['test3','input_text']


def test3fail(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Failed test, show red border"""
    page_data['test3', 'set_input_errored'] = True


def test4(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Allowed values only submitted"""
    if call_data['test4','input_text']:
        page_data['result_test4', 'para_text'] = call_data['test4','input_text']


def test5(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Allowed values only submitted"""
    if call_data['test5','test5input']:
        page_data['result_test5', 'para_text'] = call_data['test5','test5input']


def test5fail(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Failed test, show red border"""
    page_data['test5', 'set_errored'] = True

