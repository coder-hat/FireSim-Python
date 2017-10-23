# 2017-10-21
# Sandbox for learning about displaying grids of info or images
# References:
# Tkinter intro
# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
# Topic 25.1 tkinter
# https://docs.python.org/3/library/tk.html
# for a good overview:
# https://docs.python.org/3/library/tkinter.html#tkinter-life-preserver
# for grid layout manager
# http://effbot.org/tkinterbook/grid.htm

'''
A sandbox for learning about displaying grids of info or images.
'''

import tkinter as tk

class Window(tk.Frame):
    '''Creates a master widget by inheriting from the Frame class.'''
    def __init__(self, master=None):
        super().__init__(master)
        # Initialize grid geometry and cell images
        self.nrows = 7
        self.ncols = 11
        self.img_bare_ground = tk.PhotoImage(file="BareGround_32x32.png")
        self.img_conifers = tk.PhotoImage(file="Conifers_32x32.png")
        self.img_on_fire = tk.PhotoImage(file="OnFire_32x32.png")
        # Add self-configuration of additional widgets here.
        self.draw_grid()

    def draw_grid(self):
        for row in range(self.nrows):
            for col in range(self.ncols):
                img = self.img_on_fire if row == col else self.img_conifers
                tk.Label(self.master, image=img, borderwidth=0, highlightthickness=0).grid(row=row, column=col)

def main():
    root = tk.Tk()  # meant to be instantiated ONCE per application
    app = Window(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
