# 2017-10-21
'''
Toy program that simulates wildfire spread using a simple cellular automata model.
'''
import tkinter as tk
from random import random
from SquareGridGeometry import SquareGridGeometry

BARE_GROUND = 0
CONIFERS = 1
ON_FIRE = 2
BURNT_OUT = 3

class CellParameters:
    '''
    Stores the per-cell values that are immutable during simulation.
    '''
    def __init__(self, ignition_probability=0.0):
        self.ignition_probability = ignition_probability

class CellState:
    '''
    Stores mutable per-cell data for one cell in the simulation grid.
    '''
    def __init__(self, cell_type=BARE_GROUND):
        self.cell_type = cell_type

    def __str__(self):
        return str(self.cell_type)

class FireSpreadEngine:
    '''
    The simulator engine for this fire-spread model.
    '''
    NROWS = 17
    NCOLS = 21
    def __init__(self):
        self.sgg = SquareGridGeometry(cell_rows=self.NROWS, cell_cols=self.NCOLS, cell_width=32)
        self.grid = self.initialize_grid()
        self.sim_step = 0
        self.stats = {}

    def initialize_grid(self):
        '''Generates an initial map configuration.'''
        new_grid = []
        nrows = self.sgg.get_cell_rows()
        ncols = self.sgg.get_cell_cols()
        for row in range(nrows):
            cells_in_row = []
            for col in range(ncols):
                # All cells start out as conifers
                cell_type = CONIFERS
                # Unless they are on the edge of the map
                if row == 0 or row == (nrows - 1) or col == 0 or col == (ncols - 1):
                    cell_type = BARE_GROUND
                cells_in_row.append(CellState(cell_type))
            new_grid.append(cells_in_row)
        # Start a single cell near the center of the map on fire\
        new_grid[nrows // 2][ncols // 2] = CellState(ON_FIRE)
        self.cells_on_fire = 1
        return new_grid

    def step_simulation(self):
        '''
        Performs one simulation step on simulator engine's current state.
        '''
        new_grid = []
        for row in range(self.sgg.get_cell_rows()):
            cells_in_row = []
            for col in range(self.sgg.get_cell_cols()):
                cur_cell = self.grid[row][col]
                new_cell = cur_cell # default is "stay the same"
                if cur_cell.cell_type == CONIFERS:
                    burn_count = self.get_adjacent_fire_count((col, row))
                    if burn_count > 0:
                        ignite_probability = CELL_PARAMETERS_TABLE[cur_cell.cell_type].ignition_probability
                        if random() < ignite_probability:
                            new_cell = CellState(ON_FIRE)
                elif cur_cell.cell_type == ON_FIRE:
                    # currently, cells burn out after exactly one simulation step
                    new_cell = CellState(BURNT_OUT)
                cells_in_row.append(new_cell)
            new_grid.append(cells_in_row)
        self.grid = new_grid
        self.sim_step += 1

    def reset_simulation(self):
        '''Reset the simulation to its starting condtion.'''
        self.grid = self.initialize_grid()
        self.stats = self.get_current_grid_stats()

    def get_adjacent_fire_count(self, cell_location):
        '''
        Gets the number of cells (in the range [1, 4])
        adjacent to the specfied cell location that are on fire.abs
        '''
        adj_burning = 0
        for direction in range(4):
            adj_col, adj_row = self.sgg.get_adjacent_cell(cell_location, direction)
            adj_cell = self.grid[adj_row][adj_col]
            if adj_cell.cell_type == ON_FIRE:
                adj_burning += 1
        return adj_burning

    def get_current_grid_stats(self):
        '''Builds and returns a dictionary of cell_type, count pairs based on current grid.'''
        cell_counts = {}
        for row in range(self.sgg.get_cell_rows()):
            for col in range(self.sgg.get_cell_cols()):
                cur_type = self.grid[row][col].cell_type
                if cur_type not in cell_counts:
                    cell_counts[cur_type] = 0
                cell_counts[cur_type] += 1
        return cell_counts

    def print_current_grid(self):
        '''Prints an ascii dump of the current grid to stdout.'''
        for row in range(self.sgg.get_cell_rows()):
            for col in range(self.sgg.get_cell_cols()):
                sep = ' ' if col > 0 else ''
                print("{0}{1}".format(sep, self.grid[row][col]), end='')
            print()

class FireSpreadSimulatorGui(tk.Frame):
    '''Creates a master widget by inheriting from the Frame class.'''
    def __init__(self, master=None):
        super().__init__(master)
        # Initialize grid geometry and cell images
        self.image_table = {
            BARE_GROUND : tk.PhotoImage(file="BareGround_32x32.png"),
            CONIFERS : tk.PhotoImage(file="Conifers_32x32.png"),
            ON_FIRE : tk.PhotoImage(file="OnFire_32x32.png"),
            BURNT_OUT : tk.PhotoImage(file="BurntOut_32x32.png")
        }
        self.sim_engine = FireSpreadEngine()
        # Add self-configuration of additional widgets here.
        self.btn_step = tk.Button(master, text="STEP", command=self.simulator_step, borderwidth=0, highlightthickness=0)
        self.btn_reset = tk.Button(master, text="RESET", command=self.simulator_reset, borderwidth=0, highlightthickness=0)
        self.btn_step.grid(row=self.sim_engine.sgg.get_cell_rows(), column=0)
        self.btn_reset.grid(row=self.sim_engine.sgg.get_cell_rows(), column=self.sim_engine.sgg.get_cell_cols())
        # Draw initial state of the GUI
        self.display_grid = self.create_grid()

    def create_grid(self):
        '''Creates and returns a 2d grid of the Label widgets while adding them to this Frame.'''
        display_grid = []
        for row in range(self.sim_engine.sgg.get_cell_rows()):
            display_row = []
            for col in range(self.sim_engine.sgg.get_cell_cols()):
                img = self.get_image((col, row))
                label = tk.Label(self.master, image=img, borderwidth=0, highlightthickness=0)
                label.grid(row=row, column=col)
                display_row.append(label)
            display_grid.append(display_row)
        return display_grid

    def refresh_display(self):
        '''Upates the display_grid's images, based on the current state of the data grid.'''
        for row in range(self.sim_engine.sgg.get_cell_rows()):
            for col in range(self.sim_engine.sgg.get_cell_cols()):
                self.display_grid[row][col]["image"] = self.get_image((col, row))

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

CELL_PARAMETERS_TABLE = {
    BARE_GROUND : CellParameters(0.0),
    CONIFERS : CellParameters(0.5),
    ON_FIRE : CellParameters(1.0),
    BURNT_OUT : CellParameters(0.0)
}

def main():
    root = tk.Tk()  # meant to be instantiated ONCE per application
    app = FireSpreadSimulatorGui(master=root)
    app.mainloop()

if __name__ == "__main__":
    main()
