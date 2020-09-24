import tkinter.font as tkFont
from tkinter import *
from tkinter import ttk

font_family = "Helvetica"

font_size = {
    "small": 9,
    "normal": 10,
    "large": 11,
    "Large": 12
}

text_color = "#9E9E9E"

background_color = "#121212"



def initial_entry(parent):
    font_style = tkFont.Font(family = font_family, size = font_size["normal"], weight = "normal")
    return Entry(parent, bg = background_color, disabledbackground= background_color, fg = text_color, font = font_style)

def initial_menu(parent):
    font_style = tkFont.Font(family = font_family, size = font_size["large"], weight = "normal")
    return Menu(parent, bg = background_color, fg = text_color, font = font_style, tearoff =False)

def initlial_notebook(parent):
    return ttk.Notebook(parent)

def initial_frame(parent):
    frame = Frame(parent, bg = "#121212", relief = "raised")
    return frame

def initial_label_frame(parent, label):
    font_style = tkFont.Font(family = font_family, size = font_size["large"], weight = "normal")
    label_frame = LabelFrame(parent, text=label, bg="#121212", fg = text_color, font = font_style, relief = "raised")
    return label_frame

def initial_treeview(parent, show):
    style = ttk.Style(parent)
    style.theme_use("clam")
    treeview = ttk.Treeview(parent, show= show)
    return treeview

def initial_label(parent, label):
    font_style = tkFont.Font(family = font_family, size = font_size["normal"], weight = "normal")
    label = Label(parent,text=label,bg="#3B3B3B", fg = text_color, font = font_style)
    return label

def initial_button(parent, label):
    font_style = tkFont.Font(family = font_family, size = font_size["normal"], weight = "normal")
    button = Button(parent,  bg = "#212121", fg = text_color, text = label, font = font_style, relief = "raised")
    return button


def initial_checkbutton(parent, label):
    font_style = tkFont.Font(family = font_family, size = font_size["normal"], weight = "normal")
    checkbutton = Checkbutton(parent,  bg = "#212121", fg = text_color,text = label, font = font_style, relief = "raised") 
    return checkbutton

def initial_combobox(parent, options):
    font_style = tkFont.Font(family = font_family, size = font_size["normal"], weight = "normal")
    combobox = ttk.Combobox(parent, value = options, font = font_style,state = "readonly")
    return combobox
