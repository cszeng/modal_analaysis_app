from .widgets import initial_entry
from tkinter import *

def initial_message_field(parent, gv):
    message_field = initial_entry(parent)
    message_field_val = StringVar()
    gv.set_value("message_field", message_field_val) 
    message_field.configure(text = gv.var["message_field"], state=DISABLED)
    gv.var["message_field"].set("Ready")
    message_field.pack(side = BOTTOM, fill = X, padx = 3, pady =0, ipady=3) 