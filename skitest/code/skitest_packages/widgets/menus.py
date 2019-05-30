from skipole import FailPage, GoTo, ValidateError, ServerError

def modules_menu(skicall):
    """Fills in template of links to modules"""

    # each tuple in the list below is button text, link ident

    butt_list = [
                 ('error_messages', 'error_messages'),
                 ('footers', 3014),
                 ('headers', 3015),
                 ('info', 'info'),
                 ('input_forms', 3009),
                 ('inputtext', 3010),
                 ('links', 'links'),
                 ('lists', 'lists'),
                 ('logins', 'logins'),
                 ('paras', 'paras'),
                 ('svgmeters', 3018) ]


    skicall.page_data['modbuttons', 'multiplier'] = len(butt_list)
    for index,item in enumerate(butt_list):
        section_alias = 'modbuttons_' + str(index)
        skicall.page_data[section_alias, 'linkbutton', 'button_text'] = item[0]
        skicall.page_data[section_alias, 'linkbutton', 'link_ident'] = item[1]


        
