from ... import FailPage, GoTo, ValidateError, ServerError

def tagblock_test1(caller_ident, ident_list, submit_list, submit_dict, call_data, page_data, lang):
    """Changes tagblock1 to colour of drop in"""
    destination_color = call_data['tagblock2', 'drag']
    page_data['tagblock1', 'widget_style'] = "color:" + destination_color + ";margin-left:15%;width:10%;margin-right:auto;background-color:grey;text-align: center;"





