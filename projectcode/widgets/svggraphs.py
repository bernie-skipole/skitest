
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

    if 'view' in call_data:
        view = call_data['view']
        ra = call_data['rahr'] * 360.0/24.0 + call_data['ramin'] * 360.0/(24.0*60.0) +  call_data['rasec'] * 360.0/(24.0*60.0*60.0)
        dec = call_data['decdeg'] + call_data['decmin']/60.0 + call_data['decsec']/3600.0
        if call_data['decsign'] == '-':
            dec = -1.0 * dec
    else:
        view = 180.0
        ra = 0.0
        dec = 90.0
        page_data['ra_hr','input_text'] = "0"
        page_data['ra_min','input_text'] = "0"
        page_data['ra_sec','input_text'] = "0.0"
        page_data['dec_sign','input_text'] = "+"
        page_data['dec_deg','input_text'] = "90"
        page_data['dec_min','input_text'] = "0"
        page_data['dec_sec','input_text'] = "0.0"
        page_data['view','input_text'] = "180.0"



    str_ra = "{:2.8f}".format(ra)
    str_dec = "{:2.8f}".format(dec)

    # set the widget
    page_data['starchart', 'ra'] = str_ra
    page_data['starchart', 'dec'] = str_dec
    page_data['starchart', 'view'] = view
    page_data['starchart', 'transform'] = "translate(10 10)"

    # convert view to radius in arc seconds
    radius_view = str(view * 3600/2.0)

    args = ["scat", "-cd", "bsc", "-n", "800", "-r", radius_view, str_ra, str_dec, "J2000"]
    try:
        result = subprocess.check_output(args, timeout=2)
    except:
        raise FailPage("The star chart requires WCSTools to be present and working")
    if not result:
        return
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


def check_target(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Checks target ra, dec and view are valid strings"""
    failflag = False
    failmessage = "Invalid target"
 
    ra_hr = call_data['ra_hr','input_text']
    try:
        rahr = int(ra_hr)
        if (rahr > 24) or (rahr < 0):
            failflag = True
            rahr = 0
            ra_hr = ''
        elif rahr == 24:
            rahr = 0
            ra_hr = "0"
        else:
            ra_hr = str(rahr)
    except:
        failflag = True
        ra_hr = ''
        rahr = 0
    call_data['rahr'] = rahr
    page_data['ra_hr','input_text'] = ra_hr


    ra_min = call_data['ra_min','input_text']
    try:
        ramin = int(ra_min)
        if (ramin > 59) or (ramin < 0):
            failflag = True
            ra_min = ''
            ramin = 0
        else:
            ra_min = str(ramin)
    except:
        failflag = True
        ra_min = ''
        ramin = 0
    call_data['ramin'] = ramin
    page_data['ra_min','input_text'] = ra_min


    ra_sec = call_data['ra_sec','input_text']
    try:
        rasec = float(ra_sec)
        if (rasec >= 60.0) or (rasec < 0.0):
            failflag = True
            ra_sec = ''
            rasec = 0.0
        else:
            ra_sec = "{:2.1f}".format(rasec)
    except:
        failflag = True
        ra_sec = ''
        rasec = 0.0
    call_data['rasec'] = rasec
    page_data['ra_sec','input_text'] = ra_sec


    if call_data['dec_sign','input_text'] != '-':
        call_data['decsign'] = '+'
    else:
        call_data['decsign'] = '-'
    page_data['dec_sign','input_text'] = call_data['decsign']



    dec_deg = call_data['dec_deg','input_text']
    try:
        decdeg = int(dec_deg)
        if (decdeg > 90) or (decdeg < 0):
            failflag = True
            dec_deg = ''
            decdeg = 0
        else:
            dec_deg = str(decdeg)
    except:
        failflag = True
        dec_deg = ''
        decdeg = 0
    call_data['decdeg'] = decdeg
    page_data['dec_deg','input_text'] = dec_deg



    dec_min = call_data['dec_min','input_text']
    try:
        decmin = int(dec_min)
        if (decmin > 59) or (decmin < 0):
            failflag = True
            dec_min = ''
            decmin = 0
        else:
            dec_min = str(decmin)
    except:
        failflag = True
        dec_min = ''
        decmin = 0
    call_data['decmin'] = decmin
    page_data['dec_min','input_text'] = dec_min


    dec_sec = call_data['dec_sec','input_text']
    try:
        decsec = float(dec_sec)
        if (decsec >= 60.0) or (decsec < 0.0):
            failflag = True
            dec_sec = ''
            decsec = 0.0
        else:
            dec_sec = "{:2.1f}".format(decsec)
    except:
        failflag = True
        dec_sec = ''
        decsec = 0.0
    call_data['decsec'] = decsec
    page_data['dec_sec','input_text'] = dec_sec



    if not failflag:
        failmessage = "Invalid field of view"
    strview = call_data['view','input_text']
    try:
        view = float(strview)
        if (view > 270.0) or (view < 0.0):
            failflag = True
            strview = ''
            view = 90.0
        else:
            strview = "{:2.1f}".format(view)
    except:
        failflag = True
        strview = ''
        view = 90.0
    call_data['view'] = view
    page_data['view','input_text'] = strview

    if failflag:
        raise FailPage(failmessage)



