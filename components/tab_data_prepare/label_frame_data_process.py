from ..widgets import initial_label_frame, initial_button, initial_checkbutton, initial_combobox, initial_label, initial_entry
from tkinter import *
from tkinter import ttk
from functions.update_message_field import update_dir_select_message

def initial_label_frame_data_process(parent, gv):
    label_frame_data_process = initial_label_frame(parent, "Data Process")
    label_frame_data_process.configure(width = 150)
    label_frame_data_process.pack(side = LEFT, fill = Y, expand = 0, padx = 10)
    label_frame_data_process.grid_propagate(1)
    label_frame_data_process.pack_propagate(1)
    fill_label_frame_data_process(label_frame_data_process, gv)


def fill_label_frame_data_process(parent, gv):
    button_load_data = initial_button(parent,"Load Data")
    button_load_data.configure(width = 13)
    button_load_data.grid(row = 0,  columnspan = 2,padx = 3, pady = 3)

    button_struct_prop = initial_button(parent,"Struct. Prop.")
    button_struct_prop.configure(width = 13)
    button_struct_prop.grid(row = 1,  columnspan = 2,padx = 3, pady = 3)

    ttk.Separator(parent, orient = HORIZONTAL).grid(row = 2, columnspan = 2, pady = 3, sticky= W+E)

    checkbutton_x_select = initial_checkbutton(parent,"X direction")
    gv.set_value("checkbutton_x_select", IntVar())
    checkbutton_x_select.configure(width = 11, variable = gv.var["checkbutton_x_select"], command = lambda: update_dir_select_message(gv, 0))
    checkbutton_x_select.select()
    checkbutton_x_select.grid(row = 3,  columnspan = 2, padx = 3, pady = 3)
    
    checkbutton_y_select = initial_checkbutton(parent,"Y direction")
    gv.set_value("checkbutton_y_select", IntVar())
    checkbutton_y_select.configure(width = 11, variable = gv.var["checkbutton_y_select"],
    command = lambda: update_dir_select_message(gv, 1))
    checkbutton_y_select.select()
    checkbutton_y_select.grid(row = 4, columnspan = 2,padx = 3, pady = 3)

    checkbutton_z_select = initial_checkbutton(parent,"Z direction")
    gv.set_value("checkbutton_z_select", IntVar())
    checkbutton_z_select.configure(width = 11, variable = gv.var["checkbutton_z_select"],command = lambda: update_dir_select_message(gv, 2))
    checkbutton_z_select.select()
    checkbutton_z_select.grid(row = 5,  columnspan = 2,padx = 3, pady = 3)
    
    ttk.Separator(parent, orient = HORIZONTAL).grid(row = 6, columnspan = 2, pady = 3, sticky= W+E)
    
    checkbutton_demean = initial_checkbutton(parent, "Demean")
    gv.set_value("checkbutton_demean", IntVar())
    checkbutton_demean.configure(width = 11, variable = gv.var["checkbutton_demean"])
    checkbutton_demean.select()
    checkbutton_demean.grid(row = 7, columnspan = 2,padx = 3, pady = 3)

    ttk.Separator(parent, orient = HORIZONTAL).grid(row = 8, columnspan = 2,pady = 3, sticky= W+E)

    checkbutton_filter = initial_checkbutton(parent,"Filter")
    gv.set_value("checkbutton_filter", IntVar())
    checkbutton_filter.configure(width = 11, variable = gv.var["checkbutton_filter"])
    checkbutton_filter.select()
    checkbutton_filter.grid(row = 9,  columnspan = 2,padx = 3, pady = 3)

    options = ["Lowpass", "Highpass", "Bandpass", "Bandstop"]
    combobox_filter = initial_combobox(parent, options)
    combobox_filter.configure(width = 11)
    combobox_filter.current(0)
    combobox_filter.grid(row = 10, columnspan = 2,padx = 3, pady = 3)

    label_low_filter = initial_label(parent, "Low (Hz)")
    label_low_filter.configure(width = 7)
    label_low_filter.grid(row = 11, column = 0, padx = 3, pady =3)
    entry_low_filter = initial_entry(parent)
    gv.set_value("entry_low_filter", DoubleVar())
    entry_low_filter.configure(width = 6, text = gv.var["entry_low_filter"])
    gv.var["entry_low_filter"].set(0)
    entry_low_filter.grid(row = 11, column = 1, padx = 3, pady =3, sticky = N+S)

    label_high_filter = initial_label(parent, "High (Hz)")
    label_high_filter.configure(width = 7)
    label_high_filter.grid(row = 12, column = 0, padx = 1, pady =3)
    entry_high_filter = initial_entry(parent)
    gv.set_value("entry_high_filter", DoubleVar())
    entry_high_filter.configure(width = 6, text = gv.var["entry_high_filter"])
    gv.var["entry_high_filter"].set(0)
    entry_high_filter.grid(row = 12, column = 1, padx = 1, pady =3, sticky = N+S)

    label_filter_order = initial_label(parent, "Order")
    label_filter_order.configure(width = 7)
    label_filter_order.grid(row = 13, column = 0,  pady =3)
    entry_filter_order = initial_entry(parent)
    gv.set_value("entry_filter_order", IntVar())
    entry_filter_order.configure(width = 6, text = gv.var["entry_filter_order"])
    gv.var["entry_filter_order"].set(2)
    entry_filter_order.grid(row = 13, column = 1,  pady =3, sticky = N+S)

    ttk.Separator(parent, orient = HORIZONTAL).grid(row = 14, columnspan = 2, pady = 3, sticky= W+E)

    checkbutton_window = initial_checkbutton(parent,"Window")
    gv.set_value("checkbutton_window", IntVar())
    checkbutton_window.configure(width = 11, variable=gv.var["checkbutton_window"])
    gv.var["checkbutton_window"].set(1)
    checkbutton_window.grid(row = 15, columnspan = 2, pady = 3)

    options = ["Hanning", "Bartlett", "Hamming", "Blackman-Harris", "Parzen", "Taylor", "Tukey", "Kaiser","Chebyshev", "Gaussian", "Rectangluar"]
    combobox_window = initial_combobox(parent, options)
    combobox_window.configure(width = 11)
    combobox_window.current(0)
    combobox_window.grid(row = 16,columnspan=2, pady = 3)

    label_win_param = initial_label(parent, "Parm.")
    label_win_param.configure(width = 7)
    label_win_param.grid(row = 17, column = 0, pady =3)
    entry_win_param = initial_entry(parent)
    gv.set_value("entry_win_param", DoubleVar())
    entry_win_param.configure(width = 6, text = gv.var["entry_win_param"])
    gv.var["entry_win_param"].set(0)
    entry_win_param.grid(row = 17, column = 1, pady =3, sticky = N+S)

    ttk.Separator(parent, orient = HORIZONTAL).grid(row = 18, columnspan = 2, pady = 3, sticky= W+E)

    button_run = initial_button(parent, "Run")
    button_run.configure(width = 13)
    button_run.grid(row = 19, columnspan = 2, pady = 3) 