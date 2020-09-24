from ..widgets import initial_label_frame, initial_entry, initial_label, initial_button
from tkinter import *
from tkinter import ttk

def initial_label_frame_fft_control(parent, gv):
    label_frame_fft_control = initial_label_frame(parent, "FFT Control")
    label_frame_fft_control.configure(height = 120)
    label_frame_fft_control.pack(side = BOTTOM, fill = X, expand = 0, padx = 5, pady =5)
    label_frame_fft_control.grid_propagate(1)
    label_frame_fft_control.pack_propagate(1)
    fill_label_frame_fft_control(label_frame_fft_control, gv)



def fill_label_frame_fft_control(parent, gv):
    label_low_crop = initial_label(parent, "Low (Hz)")
    label_low_crop.configure(width = 7)
    label_low_crop.grid(row = 0, column = 0,  padx = 3, pady =3)
    entry_low_crop = initial_entry(parent)
    gv.set_value("entry_low_crop", DoubleVar())
    entry_low_crop.configure(width = 7, text = gv.var["entry_low_crop"])
    gv.var["entry_low_crop"].set(0.5)
    entry_low_crop.grid(row =0, column = 1, padx = 3, pady =3)
    
    label_high_crop = initial_label(parent, "High (Hz)")
    label_high_crop.configure(width = 7)
    label_high_crop.grid(row = 1, column = 0,  padx = 3, pady =3)
    entry_high_crop = initial_entry(parent)
    gv.set_value("entry_high_crop", DoubleVar())
    entry_high_crop.configure(width = 7, text = gv.var["entry_high_crop"])
    gv.var["entry_high_crop"].set(0.5)
    entry_high_crop.grid(row =1, column = 1,  padx = 3, pady =3)

    ttk.Separator(parent, orient = VERTICAL).grid(row =0, column =2 , rowspan = 2,padx = 15, sticky=N+S)

    label_fft_power = initial_label(parent, "FFT Power")
    label_fft_power.configure(width = 15)
    label_fft_power.grid(row = 0, column = 3, padx = 3, pady =3)
    entry_fft_power = initial_entry(parent)
    gv.set_value("entry_fft_power", IntVar())
    entry_fft_power.configure(width = 5, text = gv.var["entry_fft_power"])
    gv.var["entry_fft_power"].set(18)
    entry_fft_power.grid(row =0, column = 4,padx = 3,  pady =3,)

    label_win_power = initial_label(parent, "Window Power")
    label_win_power.configure(width = 15)
    label_win_power.grid(row = 1, column = 3, padx = 3, pady =3)
    entry_win_power = initial_entry(parent)
    gv.set_value("entry_win_power", IntVar())
    entry_win_power.configure(width = 5, text = gv.var["entry_win_power"])
    gv.var["entry_win_power"].set(1)
    entry_win_power.grid(row =1, column = 4,padx = 3,  pady =3)

    label_fft_resolution = initial_label(parent, "FFT Resolution")
    label_fft_resolution.configure(width = 15)
    label_fft_resolution.grid(row = 0, column = 5, padx = 3, pady =3)
    entry_fft_resolution = initial_entry(parent)
    gv.set_value("entry_fft_resolution", DoubleVar())
    entry_fft_resolution.configure(width = 5, text = gv.var["entry_fft_resolution"])
    gv.var["entry_fft_resolution"].set(0)
    entry_fft_resolution.grid(row =0, column = 6,padx = 3,  pady =3)

    ttk.Separator(parent, orient = VERTICAL).grid(row =0, column = 7 , rowspan = 2,padx = 15, sticky=N+S)

    button_fft_process = initial_button(parent, "FFT Process")
    button_fft_process.configure(width = 12)
    button_fft_process.grid(row = 0, column = 8, padx = 3, pady = 3)
    button_fft_default = initial_button(parent, "Default")
    button_fft_default.configure(width =12)
    button_fft_default.grid(row = 1, column = 8, padx = 3, pady = 3)

    