


from skipole import FailPage, GoTo, ValidateError, ServerError


def populate_chart1(skicall):
    """Sets content into chart1"""
    skicall.page_data['chart1', 'values'] = [100,50,0,-50,-100, -80, -60, -40, -20, 0, 20, 40, 60, 80]


def set_by_json(skicall):
    """Sets content into chart1"""
    skicall.page_data['chart1', 'values'] = [-100,-50,0,50,100, 80, 60, 40, 20, 0, -20, -40, -60, -80]






