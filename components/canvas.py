import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import BOTH

def initial_canvas(parent):
    figure = Figure(figsize=(5, 4),dpi = 100)
    plot = figure.add_subplot(1,1,1)
    plot.grid(True)
    canvas = FigureCanvasTkAgg(figure, parent)
    canvas.draw()
    canvas.get_tk_widget().pack(fill = BOTH, expand = 1)