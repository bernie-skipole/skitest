
import subprocess

from ... import FailPage, GoTo, ValidateError, ServerError
from .... import skilift

def populate_chart1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Sets content into chart1"""
    page_data['chart1', 'values'] = [100,50,0,-50,-100, -80, -60, -40, -20, 0, 20, 40, 60, 80]


def set_by_json(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Sets content into chart1"""
    page_data['chart1', 'values'] = [-100,-50,0,50,100, 80, 60, 40, 20, 0, -20, -40, -60, -80]



def stars(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    "Reads stars from catalogue"
    stars = []

    view = 180
    ra = "0"
    dec = "90"

    # convert view to radius in arc seconds
    radius_view = str(view * 3600/2.0)

    args = ["scat", "-cd", "bsc", "-n", "800", "-r", radius_view, ra, dec, "J2000"]
    try:
        result = subprocess.check_output(args, timeout=2)
    except:
        raise FailPage()
    if not result:
        raise FailPage()
    for line in result.split(b"\n"):
        cols = line.decode('ascii').split()
        if cols:
            # magnitude to drawn diameter
            magnitude = float(cols[3])
            if magnitude > 6.0:
                star = [0.1]
            elif magnitude > 5.0:
                star = [0.2]
            elif magnitude > 4.0:
                star = [0.5]
            elif magnitude > 3.0:
                star = [1.0]
            elif magnitude > 2.0:
                star = [2.0]
            elif magnitude > 1.0:
                star = [4.0]
            else:
                star = [6.0]
            star.append(cols[1])
            star.append(cols[2])
            stars.append(star)

    if stars:
        page_data['starchart', 'stars'] = stars

