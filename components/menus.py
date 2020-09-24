from .widgets import initial_menu

def initial_menus(parent):
    menubar = initial_menu(parent)
    parent.config(menu = menubar)

    menu_file = initial_menu(menubar)
    menubar.add_cascade(label = 'File', menu = menu_file)
    menu_file.add_command(label = "Exit", command = parent.quit)

    menu_edit = initial_menu(menubar)
    menubar.add_cascade(label = 'Edit', menu = menu_edit)

    menu_window = initial_menu(menubar)
    menubar.add_cascade(label = 'Window', menu = menu_window)

    menu_help = initial_menu(menubar)
    menubar.add_cascade(label = 'Help', menu = menu_help)
