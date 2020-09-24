from ..widgets import initial_label_frame, initial_treeview
from tkinter import *

def initial_label_frame_sensor_information(parent, gv):
    label_frame_sensor_information = initial_label_frame(parent, "Sensor Information")
    label_frame_sensor_information.configure(width = 150)
    label_frame_sensor_information.pack(side = LEFT, fill = Y, expand = 0)
    label_frame_sensor_information.grid_propagate(1)
    label_frame_sensor_information.pack_propagate(1)
    treeview_sensor_information = initial_treeview(label_frame_sensor_information, "tree")
    treeview_sensor_information.pack(side = LEFT, fill = Y, expand = 0)
    treenode_sensor_number = treeview_sensor_information.insert("", '0', "sensorNum", text = "Sensor Number")
    treenode_sensor_coordinate = treeview_sensor_information.insert("", '1', "sensorCoord", text = "Sensor Coordinate")
    