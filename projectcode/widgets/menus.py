from ... import FailPage, GoTo, ValidateError, ServerError

def modules_menu(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Fills in template of links to modules"""

    # each tuple in the list below is button text, link ident

    butt_list = [('checkbox', 'checkbox'),
                 ('confirm', 'confirm'),
                 ('debug_tools', 3012),
                 ('dropdown', 3013),
                 ('error_messages', 'error_messages'),
                 ('footers', 3014),
                 ('headers', 3015),
                 ('info', 'info'),
                 ('input_forms', 3009),
                 ('inputtables', 3016),
                 ('inputtext', 3010),
                 ('links', 'links'),
                 ('lists', 'lists'),
                 ('paras', 'paras'),
                 ('radio', 3017),
                 ('svgbasics', 3019),
                 ('svggraphs', 'svggraphs'),
                 ('svgmeters', 3018),
                 ('tables', 3020),
                 ('textarea', 3021),
                 ('upload', 3022) ]


    page_data['modbuttons', 'multiplier'] = len(butt_list)
    for index,item in enumerate(butt_list):
        section_alias = 'modbuttons_' + str(index)
        page_data[section_alias, 'linkbutton', 'button_text'] = item[0]
        page_data[section_alias, 'linkbutton', 'link_ident'] = item[1]


        
