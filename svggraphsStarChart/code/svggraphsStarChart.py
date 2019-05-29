
import os, sys

from struct import unpack

from http import cookies


# This project needs to import the skipole package, which should normally be immediately
# available if skipole has been installed on your system.

# from skipole import the WSGIApplication class which will be used to create a wsgi
# application, and exception classes which you will need in your functions

from skipole import WSGIApplication, FailPage, GoTo, ValidateError, ServerError, set_debug

# The set_debug function is used during development, it adds exception data to server error
# pages, and also stops javascript validation of input data on the client - this ensures that
# server validation can be tested

# You may also wish to import 'use_submit_list' whch can act as a decorator around your
# submit_data function. See the skipole documentation for details.

# the framework needs to know the location of the projectfiles directory holding this and
# other projects - specifically the skis and skiadmin projects
# The following line assumes, as default, that this script file is located beneath
# ...projectfiles/checkboxCheckBox1/code/

PROJECTFILES = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
PROJECT = 'svggraphsStarChart'



##############################################################################
#
# Your code needs to provide your own version of the following three functions
#
# Minimal versions are provided below, you could either develop them here,
# or more usually, create further modules and packages and import them.
#
##############################################################################


def start_call(called_ident, skicall):
    "When a call is initially received this function is called."
    return called_ident


def submit_data(skicall):
    "This function is called when a Responder wishes to submit data for processing in some manner"
    if skicall.submit_list[0] == 'stars':
        _stars(skicall)
    elif skicall.submit_list[0] == 'test1':
        _test1(skicall)
    elif skicall.submit_list[0] == 'test2':
        return _test2(skicall)                # must return here as this sets a cookie
    elif skicall.submit_list[0] == 'test3':
        return _test3(skicall)
    elif skicall.submit_list[0] == 'test4':
        return _test4(skicall)
    elif skicall.submit_list[0] == 'test5':
        return _test5(skicall)
    return


def end_call(page_ident, page_type, skicall):
    """This function is called at the end of a call prior to filling the returned page with skicall.page_data,
       it can also return an optional session cookie string."""
    return


def _stars(skicall):
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


    transform, cki = _transform_cookie(flipv, fliph, rot, skicall)
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

    # catalog file bsc5 is located under the project directory
    catalog = os.path.join(skicall.projectfiles, skicall.project, "bsc5") 

    with open(catalog, "rb") as f:
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


def _test1(skicall):
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


def _test2(skicall):
    """Rotates the chart by 20 degrees"""

    flipv, fliph, rot = _read_cookie(skicall.received_cookies)

    # Do the actual rotating
    rot += 20
    if rot >= 360:
        rot -= 360

    # get the new transform string and cookie
    transform, cki = _transform_cookie(flipv, fliph, rot, skicall)
    skicall.page_data['starchart', 'transform'] = transform
    return cki

def _test3(skicall):
    """Rotates the chart by -20 degrees"""

    flipv, fliph, rot = _read_cookie(skicall.received_cookies)

    # Do the actual rotating
    rot -= 20
    if rot < 0:
        rot += 360

    # get the new transform string and cookie
    transform, cki = _transform_cookie(flipv, fliph, rot, skicall)
    skicall.page_data['starchart', 'transform'] = transform
    return cki


def _test4(skicall):
    """Flips the chart horizontally"""

    flipv, fliph, rot = _read_cookie(skicall.received_cookies)

    # Do the actual flipping
    if fliph:
        fliph = False
    else:
        fliph = True

    # get the new transform string and cookie
    transform, cki = _transform_cookie(flipv, fliph, rot, skicall)
    skicall.page_data['starchart', 'transform'] = transform
    return cki


def _test5(skicall):
    """Flips the chart vertically"""

    flipv, fliph, rot = _read_cookie(skicall.received_cookies)

    # Do the actual flipping
    if flipv:
        flipv = False
    else:
        flipv = True

    # get the new transform string and cookie
    transform, cki = _transform_cookie(flipv, fliph, rot, skicall)
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


def _transform_cookie(flipv, fliph, rot, skicall):
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
    url_dict = skicall.projectpaths()
    cki['starchart']['path'] = url_dict[skicall.project]
    return transform, cki

    







##############################################################################
#
# The above functions will be inserted into the skipole.WSGIApplication object
# and will be called as required
#
##############################################################################


# create the wsgi application
application = WSGIApplication(project=PROJECT,
                              projectfiles=PROJECTFILES,
                              proj_data={},
                              start_call=start_call,
                              submit_data=submit_data,
                              end_call=end_call,
                              url="/")

# This creates a WSGI application object. On being created the object uses the projectfiles location to find
# and load json files which define the project, and also uses the functions :
#     start_call, submit_data, end_call
# to populate returned pages.
# proj_data is an optional dictionary which you may use for your own purposes,
# it is included as the skicall.proj_data attribute


# The skis application must always be added, without skis you're going nowhere!
# The skis sub project serves javascript files required by the framework widgets.

skis_code = os.path.join(PROJECTFILES, 'skis', 'code')
if skis_code not in sys.path:
    sys.path.append(skis_code)
import skis
skis_application = skis.makeapp(PROJECTFILES)
application.add_project(skis_application, url='/lib')

# The add_project method of application, enables the added sub application
# to be served at a URL which should extend the URL of the main 'root' application.
# The above shows the main checkboxCheckBox1 application served at "/" and the skis library
# project served at "/lib"

# Note if you want to add further sub-projects you would typically:
#     Place the sub project code location on your sys.path
#     Import the sub project to obtain its wsgi application
#     Call application.add_project with the sub project application
#     and the url where it will be served.


# to deploy on a web server, you would typically install skipole on the web server,
# together with a 'projectfiles' directory containing the projects you want
# to serve (typically this project, and the skis project).
# you would then follow the web servers own documentation which should describe how
# to load a wsgi application.

# for example, using gunicorn3 by command line

# gunicorn3 -w 4 checkboxCheckBox1:application

# Where gunicorn3 is the python3 version of gunicorn

#############################################################################
#
# You could remove everything below here when deploying and serving your
# finished application. The following lines are used to serve the project
# locally and add the skiadmin project for development.
#
#############################################################################

if __name__ == "__main__":


    ############################### THESE LINES ADD SKIADMIN FOR DEVELOPMENT ONLY #
    ###################### AND SHOULD BE REMOVED WHEN YOU DEPLOY YOUR APPLICATION #
                                                                                  #
    set_debug(True)                                                               #
    skiadmin_code = os.path.join(PROJECTFILES, 'skiadmin', 'code')                #
    if skiadmin_code not in sys.path:                                             #
        sys.path.append(skiadmin_code)                                            #
    import skiadmin                                                               #
    skiadmin_application = skiadmin.makeapp(PROJECTFILES, editedprojname=PROJECT) #
    application.add_project(skiadmin_application, url='/skiadmin')                #
                                                                                  #
    ###############################################################################

    # TYPICALLY WHEN YOUR FINISHED APPLICATION IS DEPLOYED, YOUR WEB SERVER WILL
    # IMPORT THIS MODULE AND THIS CODE WILL NEVER RUN AND COULD BE DELETED.
    # ALTERNATIVELY YOU MAY WISH TO ALTER THIS TO SERVE A DIFFERENT WEB SERVER
    # FROM THIS SCRIPT. FOR EXAMPLE, USING THE PYTHON 'WAITRESS' WEB SERVER:
    #
    # from waitress import serve
    # serve(application, host='0.0.0.0', port=8000)
    #

    from wsgiref.simple_server import make_server

    # serve the application
    host = "127.0.0.1"
    port = 8001

    httpd = make_server(host, port, application)
    print("Serving %s on port %s. Call http://localhost:%s/skiadmin to edit." % (PROJECT, port, port))
    httpd.serve_forever()

