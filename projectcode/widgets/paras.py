from ... import FailPage, GoTo, ValidateError, ServerError

def tagblock_test1(skicall):
    """Changes tagblock1 to colour of drop in"""
    destination_color = skicall.call_data['tagblock2', 'drag']
    skicall.page_data['tagblock1', 'widget_style'] = "color:" + destination_color + ";margin-left:15%;width:10%;margin-right:auto;background-color:grey;text-align: center;"





