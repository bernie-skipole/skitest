from skipole import FailPage, GoTo, ValidateError, ServerError

def goto_test3(skicall):
    """Tests GoTo can call a labelled page in a sub project"""
    raise GoTo(target = 'skis,test1')


