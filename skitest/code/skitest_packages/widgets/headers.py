from ... import FailPage, GoTo, ValidateError, ServerError

def widgets_menu(skicall):
    """Fills in template of links to widget tests"""

    # each tuple in the list below is button text, link ident

    butt_list = [('NavButtons1', 'home'),
                 ('NavButtons2', 'home'),
                 ('TabButtons1', 'home'),
                 ('DropDownButton1', 'home'),
                 ('HeaderErrorPara', 'home'),
                 ('HeadText', 'home'),
                 ('HeaderText1', 'home'),
                 ('HeaderText2', 'home'),
                 ('HeaderText3', 'home'),
                 ('HeaderText4', 'home'),
                 ('HeaderText5', 'home'),
                 ('HeaderText6', 'home') ]


    skicall.page_data['widgetbuttons', 'multiplier'] = len(butt_list)
    for index,item in enumerate(butt_list):
        section_alias = 'widgetbuttons_' + str(index)
        skicall.page_data[section_alias, 'linkbutton', 'button_text'] = item[0]
        skicall.page_data[section_alias, 'linkbutton', 'link_ident'] = item[1]


        
