from skipole import FailPage, GoTo, ValidateError, ServerError

def responders_menu(skicall):
    """Fills in template of links to responder tests"""

    # each tuple in the list below is button text, link ident

    butt_list = [('Accept', 'home'),
                 ('AllowAccept', 'home'),
                 ('AllowedFields', 'home'),
                 ('AllowStore', 'home'),
                 ('AllowStoreKeyed', 'home'),
                 ('CaseSwitch', 'home'),
                 ('ColourSubstitute', 'home'),
                 ('DelCallDataItem', 'home'),
                 ('EmptyCallDataGoto', 'home'),
                 ('EmptyGoto', 'home'),
                 ('FieldStoreSubmit', 'home'),
                 ('GetDictionaryDefaults', 'home'),
                 ('LanguageCookie', 'home'),
                 ('NoOperation', 'home'),
                 ('MediaQuery', 201501),
                 ('PageData', 'home'),
                 ('PrettyFormData', 'home'),
                 ('SetCookies', 'home'),
                 ('StoreData','home'),
                 ('StoreDataKeyed', 'home'),
                 ('SubmitCSS', 202101),
                 ('SubmitData', 'home'),
                 ('SubmitIterator', 'home'),
                 ('SubmitJSON', 'home'),
                 ('SubmitPlainText', 'home') ]


    skicall.page_data['responderbuttons', 'multiplier'] = len(butt_list)
    for index,item in enumerate(butt_list):
        section_alias = 'responderbuttons_' + str(index)
        skicall.page_data[section_alias, 'linkbutton', 'button_text'] = item[0]
        skicall.page_data[section_alias, 'linkbutton', 'link_ident'] = item[1]


        
