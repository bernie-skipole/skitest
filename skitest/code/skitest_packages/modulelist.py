

from skipole.skilift import editwidget

from skipole import ServerError, FailPage, ValidateError, GoTo



def retrieve_module_list(skicall):
    "this call is to retrieve data for listing widget modules"

    # table of widget modules

    # col 0 is the visible text to place in the link,
    # col 1 is the get field of the link
    # col 2 is the get field of the link
    # col 3 is the reference string of a textblock to appear in the column adjacent to the link
    # col 4 is text to appear if the reference cannot be found in the database
    # col 5 normally empty string, if set to text it will replace the textblock

    contents = []

    modules_tuple = editwidget.widget_modules()

    for name in modules_tuple:
        ref = 'widgets.' + name + '.module'
        notfound = 'Textblock reference %s not found' % ref
        contents.append([name, name, '', ref, notfound, ''])

    skicall.page_data[("modules","link_table")] = contents


def retrieve_widgets_list(skicall):
    "this call is to retrieve data for listing widgets in a module"

    call_data = skicall.call_data
    page_data = skicall.page_data

    if 'module' in call_data:
        module_name = call_data['module']
    else:
        raise FailPage("Module not identified")

    modules_tuple = editwidget.widget_modules()

    if module_name not in modules_tuple:
        raise FailPage("Module not identified")

    # set module into call_data
    call_data['module'] = module_name

    page_data[("adminhead","page_head","large_text")] = "Widgets in module %s" % (module_name,)
    page_data[('moduledesc','textblock_ref')] = 'widgets.' + module_name + '.module'

    # table of widgets

    # col 0 is the visible text to place in the link,
    # col 1 is the get field of the link
    # col 2 is the get field of the link
    # col 3 is the reference string of a textblock to appear in the column adjacent to the link
    # col 4 is text to appear if the reference cannot be found in the database
    # col 5 normally empty string, if set to text it will replace the textblock

    widget_list = editwidget.widgets_in_module(module_name)
    contents = []
    for widget in widget_list:
        ref = ".".join(("widgets", module_name, widget.classname))
        notfound = 'Textblock reference %s not found' % ref
        classname = widget.classname
        contents.append([classname, classname, '', ref, notfound, ''])

    page_data[("widgets","link_table")] = contents


