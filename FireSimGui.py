# 2017-10-21
'''
Graphical User Interface for FireSimEngine instance.
'''
import tkinter as tk
from tkinter import ttk

from FireSimEngine import FireSimEngine
from FireSimEngine import CellParameters
from FireSimEngine import BARE_GROUND
from FireSimEngine import CONIFERS
from FireSimEngine import ON_FIRE
from FireSimEngine import BURNT_OUT


class FireSimGui(tk.Frame):
    '''Creates a master widget by inheriting from the Frame class.'''
    def __init__(self, master=None):
        super().__init__(master)

        master.title(string="Fire Spread Simulator")

        # specify custom style for widgets in the display grid
        # self.s = ttk.Style()
        # self.s.configure('Grid.TLabel', borderwith=10)

        # Initialize grid geometry and cell images
        self.image_table = {
            BARE_GROUND : tk.PhotoImage(file="BareGround_32x32.png"),
            CONIFERS : tk.PhotoImage(file="Conifers_32x32.png"),
            ON_FIRE : tk.PhotoImage(file="OnFire_32x32.png"),
            BURNT_OUT : tk.PhotoImage(file="BurntOut_32x32.png")
        }
        self.sim_engine = FireSimEngine()

        # Draw initial state of the GUI
        self.display_grid = self.create_grid()

        # Add self-configuration of additional widgets here.
        r_count = self.sim_engine.sgg.get_cell_rows()
        c_count = self.sim_engine.sgg.get_cell_cols()
        self.btn_step = tk.Button(master, text="STEP", command=self.simulator_step, bg='lightblue')
        self.statusText = tk.StringVar()
        self.lblStatus = tk.Label(self.master, textvariable=self.statusText, borderwidth=0, highlightthickness=0)
        self.btn_reset = tk.Button(master, text="RESET", command=self.simulator_reset, bg='lightblue')
        self.btn_step.grid(row=r_count, column=0, columnspan=2, sticky='we')
        self.lblStatus.grid(row=r_count, column=2, columnspan=c_count-4, sticky='we')
        self.btn_reset.grid(row=r_count, column=c_count-2, columnspan=2, sticky='we')

        # cache the background color
        self.default_bg = self.master['background']

    # NOTE 2019-1-25 
    # Possible future code left as comment/example below

    # def bg_color_on_mouse_enter(self, event):
    #     event.widget.configure(background='black')
    
    # def bg_color_on_mouse_leave(self, event):
    #     event.widget.configure(background=self.default_bg)

    def create_grid(self):
        '''Creates and returns a 2d grid of the Label widgets while adding them to this Frame.'''
        display_grid = []
        for row in range(self.sim_engine.sgg.get_cell_rows()):
            display_row = []
            for col in range(self.sim_engine.sgg.get_cell_cols()):
                img = self.get_image((col, row))
                # NOTE 2019-1-25
                # Following statement is commented out because it doesn't work under Mac OSX:
                #   the border and highlightthickness args are ignored.
                #label = tk.Label(self.master, image=img, borderwidth=0, highlightthickness=0)
                # Following statement also doesn't work under Mac OSX:
                #   even when Grid.TLabel is configured (see commented-out code in __init__), style is ignored. 
                #label = ttk.Label(self.master, image=img, style='Grid.TLabel')
                # However, the following statement DOES work under Mac OSX:
                #   no border, and no highlightthickness are added to the label(s).
                label = ttk.Label(self.master, image=img, borderwidth=0)
                label.grid(row=row, column=col)
                # NOTE 2019-1-25 
                # Possible future code left as comment/example below
                # label.bind('<Enter>', self.bg_color_on_mouse_enter)
                # label.bind('<Leave>', self.bg_color_on_mouse_leave)
                display_row.append(label)
            display_grid.append(display_row)
        return display_grid

    def refresh_display(self):
        '''Upates the display_grid's images, based on the current state of the data grid.'''
        for row in range(self.sim_engine.sgg.get_cell_rows()):
            for col in range(self.sim_engine.sgg.get_cell_cols()):
                self.display_grid[row][col]["image"] = self.get_image((col, row))
        self.statusText.set(self.sim_engine.get_current_grid_stats_text())

    def get_image(self, cell_location):
        col, row = cell_location
        cur_cell = self.sim_engine.grid[row][col]
        return self.image_table[cur_cell.cell_type]

    def simulator_step(self):
        self.sim_engine.step_simulation()
        self.refresh_display()

    def simulator_reset(self):
        self.sim_engine.reset_simulation()
        self.refresh_display()
