from components.main_window import initial_main_window

class Window():
    def __init__(self, gv):
        self.root = initial_main_window(gv)

class GlobalVar():
    def __init__(self):
        self.var = {}
    
    def set_value(self, key, value):
        self.var[key] = value
    
    def get_value(self, key):
        try:
            return self.var[key].get()
        except KeyError:
            return None

if __name__ == "__main__":
    gv = GlobalVar()
    app = Window(gv)
    app.root.mainloop()


