import tkinter as tk
from tkinter import ttk

from SquareGridGeometry import SquareGridGeometry

def create_grid(master, sgg, img):
    display_grid = []
    for row in range(sgg.get_cell_rows()):
        display_row = []
        for col in range(sgg.get_cell_cols()):
            label = ttk.Label(master, image=img, style='Grid.TLabel') #, borderwidth=0, highlightthickness=0)
            label.grid(row=row, column=col)
            display_row.append(label)
        display_grid.append(display_row)
    return display_grid

if __name__ == "__main__":

    window = tk.Tk()
    s = ttk.Style()
    s.configure('Grid.TLabel', borderwidth=7)
    
    sgg = SquareGridGeometry(cell_rows=3, cell_cols=3)
    img =tk.PhotoImage(file="Conifers_32x32.png")
    label_grid = create_grid(window, sgg, img)
    
    window.mainloop()