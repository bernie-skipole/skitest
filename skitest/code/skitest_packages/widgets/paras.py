from ... import FailPage, GoTo, ValidateError, ServerError

def tagblock_test1(skicall):
    """Changes tagblock1 to colour of drop in"""
    destination_color = skicall.call_data['tagblock2', 'drag']
    skicall.page_data['tagblock1', 'widget_style'] = "color:" + destination_color + ";margin-left:15%;width:10%;margin-right:auto;background-color:grey;text-align: center;"




def divhtml_test2(skicall):
    """Changes divhtml widget content"""
    skicall.page_data['divhtml', 'set_html'] = """<p>This
is
a
paragraph<br />with two lines</p><p>And this is a second one line paragraph</p>"""





