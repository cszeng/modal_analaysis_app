from .widgets import initlial_notebook, initial_frame
from tkinter import BOTH
from .tab_data_prepare.label_frame_fft_control import initial_label_frame_fft_control
from .tab_data_prepare.label_frame_sensor_information import initial_label_frame_sensor_information
from .tab_data_prepare.label_frame_data_process import initial_label_frame_data_process
from .tab_data_prepare.label_frame_data_visualization import initial_label_frame_data_visualization


def initial_tabs(parent, gv):
    tab_parent = initlial_notebook(parent)
    tab_parent.pack(pady = 5)
    tab_parent.pack(expand=1, fill= BOTH)

    tab_data_prepare = initial_frame(tab_parent)
    tab_parent.add(tab_data_prepare, text = 'Data Preparation')

    initial_label_frame_fft_control(tab_data_prepare, gv)
    initial_label_frame_sensor_information(tab_data_prepare, gv)
    initial_label_frame_data_process(tab_data_prepare, gv)
    initial_label_frame_data_visualization(tab_data_prepare, gv)
    
    tab_mode_selection = initial_frame(tab_parent)
    tab_parent.add(tab_mode_selection, text = 'Mode Selection')

    tab_output = initial_frame(tab_parent)
    tab_parent.add(tab_output, text = 'Output')




    