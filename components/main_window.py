import tkinter as tk
from .menus import initial_menus
from .message_field import initial_message_field
from .tabs import initial_tabs

def initial_main_window(gv):
    root = tk.Tk()
    root.geometry("1100x750")
    root.title("Modal Analysis")
    root.iconbitmap(".\icons\\app.ico")

    # initialize menu bars
    initial_menus(root)

    # initlialize message field
    initial_message_field(root, gv)

    # initialize tabs
    initial_tabs(root, gv)

    
    return root


