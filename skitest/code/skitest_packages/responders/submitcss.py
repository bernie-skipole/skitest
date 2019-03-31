from ... import FailPage, GoTo, ValidateError, ServerError

def test_blue(skicall):
    """Tests submitcss by returning a css style makeblue, white text on a blue background"""
    return { '.makeblue': [['background-color', 'blue'],
                           ['color', 'white'],
                           ['margin', '10px'],
                           ['padding', '10px']
                           ] }


def test_invblue(skicall):
    """Tests submitcss by returning a css style makeblue, blue text on a white background"""
    return { '.makeblue': [['background-color', 'white'],
                           ['color', 'blue'],
                           ['margin', '10px'],
                           ['padding', '10px']
                           ] }
