
from struct import unpack

from http import cookies

from ....skilift import FailPage, GoTo, ValidateError, ServerError, projectURLpaths


def populate_chart1(skicall):
    """Sets content into chart1"""
    skicall.page_data['chart1', 'values'] = [100,50,0,-50,-100, -80, -60, -40, -20, 0, 20, 40, 60, 80]


def set_by_json(skicall):
    """Sets content into chart1"""
    skicall.page_data['chart1', 'values'] = [-100,-50,0,50,100, 80, 60, 40, 20, 0, -20, -40, -60, -80]



def stars(skicall):
    "Reads stars from catalogue"
    stars = []

    if 'view' in skicall.call_data:
        view = skicall.call_data['view']
        ra = skicall.call_data['rahr'] * 360.0/24.0 + skicall.call_data['ramin'] * 360.0/(24.0*60.0) +  skicall.call_data['rasec'] * 360.0/(24.0*60.0*60.0)
        dec = skicall.call_data['decdeg'] + skicall.call_data['decmin']/60.0 + skicall.call_data['decsec']/3600.0
        if skicall.call_data['decsign'] == '-':
            dec = -1.0 * dec
    else:
        view = 180.0
        ra = 0.0
        dec = 90.0
        skicall.page_data['ra_hr','input_text'] = "0"
        skicall.page_data['ra_min','input_text'] = "0"
        skicall.page_data['ra_sec','input_text'] = "0.0"
        skicall.page_data['dec_sign','input_text'] = "+"
        skicall.page_data['dec_deg','input_text'] = "90"
        skicall.page_data['dec_min','input_text'] = "0"
        skicall.page_data['dec_sec','input_text'] = "0.0"
        skicall.page_data['view','input_text'] = "180.0"


    # read the cookie
    flipv, fliph, rot = _read_cookie(skicall.received_cookies)
    # get the transform string and cookie


    transform, cki = _transform_cookie(flipv, fliph, rot, skicall.project)
    # set the transform
    skicall.page_data['starchart', 'transform'] = transform

    str_ra = "{:2.8f}".format(ra)
    str_dec = "{:2.8f}".format(dec)

    # set the widget
    skicall.page_data['starchart', 'ra'] = str_ra
    skicall.page_data['starchart', 'dec'] = str_dec
    skicall.page_data['starchart', 'view'] = view

    max_dec = dec + view/2.0
    min_dec = dec - view/2.0

    with open("/home/bernie/test/astrodata/bsc5_remscope", "rb") as f:
        while True:
            bstar = f.read(12)
            if not bstar:
                break
            ra_degrees, dec_degrees, magnitude = unpack('fff', bstar)
            if dec_degrees > max_dec:
                continue
            if dec_degrees < min_dec:
                continue
            if magnitude > 6.0:
                star = [0.1, ra_degrees, dec_degrees]
            elif magnitude > 5.0:
                star = [0.2, ra_degrees, dec_degrees]
            elif magnitude > 4.0:
                star = [0.5, ra_degrees, dec_degrees]
            elif magnitude > 3.0:
                star = [1.0, ra_degrees, dec_degrees]
            elif magnitude > 2.0:
                star = [2.0, ra_degrees, dec_degrees]
            elif magnitude > 1.0:
                star = [4.0, ra_degrees, dec_degrees]
            else:
                star = [6.0, ra_degrees, dec_degrees]
            stars.append(star)

    if stars:
        skicall.page_data['starchart', 'stars'] = stars


def check_target(skicall):
    """Checks target ra, dec and view are valid strings"""
    failflag = False
    failmessage = "Invalid target"
 
    ra_hr = skicall.call_data['ra_hr','input_text']
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
    skicall.call_data['rahr'] = rahr
    skicall.page_data['ra_hr','input_text'] = ra_hr


    ra_min = skicall.call_data['ra_min','input_text']
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
    skicall.call_data['ramin'] = ramin
    skicall.page_data['ra_min','input_text'] = ra_min


    ra_sec = skicall.call_data['ra_sec','input_text']
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
    skicall.call_data['rasec'] = rasec
    skicall.page_data['ra_sec','input_text'] = ra_sec


    if skicall.call_data['dec_sign','input_text'] != '-':
        skicall.call_data['decsign'] = '+'
    else:
        skicall.call_data['decsign'] = '-'
    skicall.page_data['dec_sign','input_text'] = skicall.call_data['decsign']



    dec_deg = skicall.call_data['dec_deg','input_text']
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
    skicall.call_data['decdeg'] = decdeg
    skicall.page_data['dec_deg','input_text'] = dec_deg



    dec_min = skicall.call_data['dec_min','input_text']
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
    skicall.call_data['decmin'] = decmin
    skicall.page_data['dec_min','input_text'] = dec_min


    dec_sec = skicall.call_data['dec_sec','input_text']
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
    skicall.call_data['decsec'] = decsec
    skicall.page_data['dec_sec','input_text'] = dec_sec



    if not failflag:
        failmessage = "Invalid field of view"
    strview = skicall.call_data['view','input_text']
    try:
        view = float(strview)
        if (view > 360.0) or (view < 0.01):
            failflag = True
            strview = ''
            view = 90.0
        else:
            strview = "{:2.1f}".format(view)
    except:
        failflag = True
        strview = ''
        view = 90.0
    skicall.call_data['view'] = view
    skicall.page_data['view','input_text'] = strview

    if failflag:
        raise FailPage(failmessage)


def rotate_plus(skicall):
    """Rotates the chart by 20 degrees"""

    flipv, fliph, rot = _read_cookie(skicall.received_cookies)

    # Do the actual rotating
    rot += 20
    if rot >= 360:
        rot -= 360

    # get the new transform string and cookie
    transform, cki = _transform_cookie(flipv, fliph, rot, skicall.project)
    skicall.page_data['starchart', 'transform'] = transform
    return cki

def rotate_minus(skicall):
    """Rotates the chart by -20 degrees"""

    flipv, fliph, rot = _read_cookie(skicall.received_cookies)

    # Do the actual rotating
    rot -= 20
    if rot < 0:
        rot += 360

    # get the new transform string and cookie
    transform, cki = _transform_cookie(flipv, fliph, rot, skicall.project)
    skicall.page_data['starchart', 'transform'] = transform
    return cki



def flip_v(skicall):
    """Flips the chart vertically"""

    flipv, fliph, rot = _read_cookie(skicall.received_cookies)

    # Do the actual flipping
    if flipv:
        flipv = False
    else:
        flipv = True

    # get the new transform string and cookie
    transform, cki = _transform_cookie(flipv, fliph, rot, skicall.project)
    skicall.page_data['starchart', 'transform'] = transform
    return cki


def flip_h(skicall):
    """Flips the chart horizontally"""

    flipv, fliph, rot = _read_cookie(skicall.received_cookies)

    # Do the actual flipping
    if fliph:
        fliph = False
    else:
        fliph = True

    # get the new transform string and cookie
    transform, cki = _transform_cookie(flipv, fliph, rot, skicall.project)
    skicall.page_data['starchart', 'transform'] = transform
    return cki


def _read_cookie(received_cookies):
    "Reads cookie, and returns flipv, fliph, rot"
    rot = 0
    flipv = False
    fliph = False
    if 'starchart' in received_cookies:
        clist = received_cookies['starchart'].split(':')
        if len(clist) == 3:
            flipv = True if clist[0] == '1' else False
            fliph = True if clist[1] == '1' else False
            if clist[2]:
                rot = int(clist[2])
            else:
                rot = 0
    return flipv, fliph, rot


def _transform_cookie(flipv, fliph, rot, project):
    "Returns transform_string, cookie"
    # set the widget transform attribute
    if flipv and fliph:
        transform = "translate(510 510) scale(-1)"
    elif flipv:
        transform = "translate(10 510) scale(1, -1)"
    elif fliph:
        transform = "translate(510 10) scale(-1, 1)"
    else:
        transform = "translate(10 10)"

    if rot:
        transform += " rotate(" + str(rot) + ",250,250)"

    # set a cookie for cookie key 'starchart'
    if flipv:
        ck_string = "1:"
    else:
        ck_string = "0:"
    if fliph:
        ck_string += "1:"
    else:
        ck_string += "0:"
    ck_string += str(rot)
    cki = cookies.SimpleCookie()
    cki['starchart'] = ck_string
    # twelve hours expirey time
    cki['starchart']['max-age'] = 43200
    # set root project path
    url_dict = projectURLpaths()
    cki['starchart']['path'] = url_dict[project]
    return transform, cki

    




