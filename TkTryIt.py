# 2017-10-21
# Sandbox for Tkinter learning and experiments
# References:
# Tkinter intro
# https://pythonprogramming.net/python-3-tkinter-basics-tutorial/
# Topic 25.1 tkinter
# https://docs.python.org/3/library/tk.html
'''
A sandbox for learning and experiments with Tkinter grid manager.
'''

import tkinter as tk

class Window(tk.Frame):
    '''Creates a master widget by inheriting from the Frame class.'''

    def __init__(self, master=None):
        super().__init__(master)

        # Initialize grid geometry and images
        self.ncols = 11
        self.nrows = 7
        self.image_conifers = tk.PhotoImage("Conifers_32x32.png")
        self.image_bare_ground = tk.PhotoImage("BareGround_32x32.png")
        self.image_fire = tk.PhotoImage("OnFire_32x32.png")
        # Add self-configuration of additional widgets here.
        self.draw_grid()

    def draw_grid(self):
        for r in range(self.nrows):
            for c in range(self.ncols):
                bg_image = self.image_conifers
                tk.Label(self.master, fg=bg_image).grid(row=r, column=c)
                print("Placed Label at row={0} col={1]}".format(r, c))


def main():
    root = tk.Tk()  # meant to be instantiated ONCE per application
    app = Window(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
