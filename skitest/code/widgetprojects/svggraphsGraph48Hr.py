
from datetime import datetime, timedelta

from skipole import WSGIApplication, FailPage, GoTo, ValidateError, ServerError, set_debug


def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    return called_ident


def submit_data(skicall):
    "This function is called when a Responder wishes to submit data for processing in some manner"
    skicall.page_data['graph', 'values'] = _graph48hr()

def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return


def _graph48hr():
    "Returns a table of points to be displayed on a graph48hr widget"
    hr = timedelta(hours=1)
    t = datetime.now()
    t = t.replace(minute=0, second=0, microsecond=0)
    t = t - timedelta(days=2)
    result = []
    for n in range(0, 24):
        t = t + hr
        result.append((n+30, t))
    for n in range(24, 48):
        t = t + hr
        result.append((77-n, t))
    return result


def makeapp(projectfiles, **proj_data):
    """returns the application"""
    return WSGIApplication(project='svggraphsGraph48Hr',
                           projectfiles=projectfiles,
                           proj_data=proj_data,
                           start_call=start_call,
                           submit_data=submit_data,
                           end_call=end_call,
                           url="/")

