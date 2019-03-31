def test1(skicall):
    """Allowed values only submitted"""
    if skicall.call_data['test1','input_text']:
        skicall.page_data['result_test1', 'para_text'] = skicall.call_data['test1','input_text']


def test2(skicall):
    """Allowed values only submitted"""
    if skicall.call_data['test2','input_text']:
        skicall.page_data['result_test2', 'para_text'] = skicall.call_data['test2','input_text']


def test2fail(skicall):
    """Failed test, show red border"""
    skicall.page_data['test2', 'set_input_errored'] = True


def test3(skicall):
    """Allowed values only submitted"""
    if skicall.call_data['test3','input_text']:
        skicall.page_data['result_test3', 'para_text'] = skicall.call_data['test3','input_text']


def test3fail(skicall):
    """Failed test, show red border"""
    skicall.page_data['test3', 'set_input_errored'] = True


def test4(skicall):
    """Allowed values only submitted"""
    if skicall.call_data['test4','input_text']:
        skicall.page_data['result_test4', 'para_text'] = skicall.call_data['test4','input_text']


def test5(skicall):
    """Allowed values only submitted"""
    if skicall.call_data['test5','test5input']:
        skicall.page_data['result_test5', 'para_text'] = skicall.call_data['test5','test5input']


def test5fail(skicall):
    """Failed test, show red border"""
    skicall.page_data['test5', 'set_errored'] = True


def test6(skicall):
    """Allowed values only submitted"""
    if skicall.call_data['test6','test6','test6input']:
        skicall.page_data['test6', 'result_test6', 'para_text'] = skicall.call_data['test6','test6','test6input']


def test6fail(skicall):
    """Failed test, show red border"""
    skicall.page_data['test6', 'test6', 'set_errored'] = True

