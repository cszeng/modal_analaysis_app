from ..widgets import initial_label_frame, initial_button, initial_checkbutton, initial_label, initial_entry, initial_frame
from tkinter import *
from tkinter import ttk
from ..canvas import initial_canvas

def initial_label_frame_data_visualization(parent, gv):
    label_frame_data_visualization = initial_label_frame(parent, "Data Visualization")
    label_frame_data_visualization.pack(side = RIGHT, fill = BOTH, expand = 1)
    label_frame_data_visualization.grid_propagate(0)
    label_frame_data_visualization.pack_propagate(0)

    frame_bottom = initial_frame(label_frame_data_visualization)
    frame_bottom.grid_propagate(0)
    frame_bottom.pack_propagate(0)
    frame_bottom.configure(height = 70)
    frame_bottom.pack(side = BOTTOM, fill =X, expand = 0, padx =5, pady = 5,ipadx= 1, ipady =1)
    fill_frame_bottom(frame_bottom, gv)

    frame_top = initial_frame(label_frame_data_visualization)
    frame_top.grid_propagate(0)
    frame_top.pack_propagate(0)
    frame_top.pack(side = TOP, fill =BOTH, expand = 1, padx =5, pady = 3, ipadx= 1, ipady =1)
    initial_canvas(frame_top)


def fill_frame_bottom(parent, gv):
    checkbutton_x_dir = initial_checkbutton(parent, "X")
    gv.set_value("checkbutton_x_dir", IntVar())
    checkbutton_x_dir.configure(width = 3, variable = gv.var["checkbutton_x_dir"])
    checkbutton_x_dir.select()
    checkbutton_x_dir.grid(row=0, column = 0, padx = 4, pady =4,sticky=NSEW )

    checkbutton_y_dir = initial_checkbutton(parent, "Y")
    gv.set_value("checkbutton_y_dir", IntVar())
    checkbutton_y_dir.configure(width = 3, variable = gv.var["checkbutton_y_dir"])
    checkbutton_y_dir.select()
    checkbutton_y_dir.grid(row=1, column = 0, padx = 4, pady =4,sticky=NSEW  )

    checkbutton_z_dir = initial_checkbutton(parent, "Z")
    gv.set_value("checkbutton_z_dir", IntVar())
    checkbutton_z_dir.configure(width = 3, variable = gv.var["checkbutton_z_dir"])
    checkbutton_z_dir.select()
    checkbutton_z_dir.grid(row=0, column = 1,padx = 4, pady =4, sticky=NSEW)

    checkbutton_r_dir = initial_checkbutton(parent, "R")
    gv.set_value("checkbutton_r_dir", IntVar())
    checkbutton_r_dir.configure(width = 3, variable = gv.var["checkbutton_r_dir"])
    checkbutton_r_dir.select()
    checkbutton_r_dir.grid(row=1, column = 1, padx = 4, pady =4,sticky=NSEW)

    ttk.Separator(parent, orient = VERTICAL).grid(row =0, column =2 , rowspan = 2,padx = 8,pady = 4, sticky=N+S)

    checkbutton_data_grid = initial_checkbutton(parent,"Grid")
    gv.set_value("checkbutton_data_grid", IntVar())
    checkbutton_data_grid.configure(width = 7, variable = gv.var["checkbutton_data_grid"])
    checkbutton_data_grid.select()
    checkbutton_data_grid.grid(row=0, column = 3, padx = 4, pady = 4,sticky=NSEW )

    checkbutton_data_legend = initial_checkbutton(parent,"Legend")
    gv.set_value("checkbutton_data_legend", IntVar())
    checkbutton_data_legend.configure(width = 7, variable = gv.var["checkbutton_data_legend"])
    checkbutton_data_legend.select()
    checkbutton_data_legend.grid(row=1, column = 3, padx = 4, pady = 4,sticky=NSEW )

    ttk.Separator(parent, orient = VERTICAL).grid(row =0, column = 4 , rowspan = 2,padx = 8,pady = 4, sticky=N+S)

    label_data_linewidth = initial_label(parent, "Line Width")
    label_data_linewidth.configure(width = 10)
    label_data_linewidth.grid(row=0, column = 5, padx = 4, pady = 4, sticky = NSEW)
    entry_data_linewidth = initial_entry(parent)
    gv.set_value("entry_data_linewidth", DoubleVar())
    entry_data_linewidth.configure(width = 10, text = gv.var["entry_data_linewidth"])
    gv.var["entry_data_linewidth"].set(1)
    entry_data_linewidth.grid(row = 1, column =5, padx = 4, pady = 4, sticky = NSEW)

    ttk.Separator(parent, orient = VERTICAL).grid(row =0, column = 6 , rowspan = 2,padx = 8,pady = 4, sticky=N+S)

    checkbutton_fft_cum = initial_checkbutton(parent,"Cumulative")
    gv.set_value("checkbutton_fft_cum", IntVar())
    checkbutton_fft_cum.configure(width = 11, variable = gv.var["checkbutton_fft_cum"])
    checkbutton_fft_cum.deselect()
    checkbutton_fft_cum.grid(row=0, column = 7, padx = 4, pady = 4,sticky=NSEW )

    checkbutton_fft_norm = initial_checkbutton(parent,"Normalization")
    gv.set_value("checkbutton_fft_norm", IntVar())
    checkbutton_fft_norm.configure(width = 11, variable = gv.var["checkbutton_fft_norm"])
    checkbutton_fft_norm.deselect()
    checkbutton_fft_norm.grid(row=1, column = 7, padx = 4, pady = 4,sticky=NSEW )

    button_fft_plot = initial_button(parent, "FFT Plot")
    button_fft_plot.configure(width = 14)
    button_fft_plot.grid(row=0, column = 8,padx = 4, pady = 4,sticky=NSEW )

    button_timehis_plot = initial_button(parent, "Time History Plot")
    button_timehis_plot.configure(width = 14)
    button_timehis_plot.grid(row=1, column = 8, padx = 4, pady = 4,sticky=NSEW )

    ttk.Separator(parent, orient = VERTICAL).grid(row =0, column = 9 , rowspan = 2,padx = 8,pady = 4, sticky=N+S)

    button_save = initial_button(parent, "Save")
    button_save.configure(width = 7)
    button_save.grid(row=0, column = 10, rowspan = 2, padx = 4, pady = 4,sticky=NSEW )