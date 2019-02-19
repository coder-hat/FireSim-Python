# 2017-10-21
'''
Very simplified wildfire spread simulator, using a simple cellular automata model.
In this model:
1. Only CONIFERS cells can burn.
2. ON_FIRE cells burn out when their fuel amount reaches zero.
3. Burning reduces a cells fuel by a fixed amount each simulation step.
4. CONIFERS cells have a increasing probability of catching fire
   based on the number of adjacent ON_FIRE cells (0.25 per cell). 
'''
import random
from SquareGridGeometry import SquareGridGeometry

BARE_GROUND = 0
CONIFERS = 1
ON_FIRE = 2
BURNT_OUT = 3

CELL_TYPE_NAMES = ['Bare Ground', 'Conifers', 'On Fire', 'Burnt Out']


class CellParameters:
    '''
    Stores the per-cell values that are immutable during simulation.
    '''
    def __init__(self, ignition_probability=0.0):
        self.ignition_probability = ignition_probability

CELL_PARAMETERS_TABLE = {
    BARE_GROUND : CellParameters(0.0),
    CONIFERS : CellParameters(0.5),
    ON_FIRE : CellParameters(1.0),
    BURNT_OUT : CellParameters(0.0)
}

MIN_FUEL = 1
MAX_FUEL = 4


class CellState:
    '''
    Stores mutable per-cell data for one cell in the simulation grid.
    '''
    def __init__(self, cell_type=BARE_GROUND, cell_fuel=None):
        self.cell_type = cell_type
        if cell_fuel == None:
            self.cell_fuel = MAX_FUEL if self.cell_type == CONIFERS else 0
        else:
            self.cell_fuel = cell_fuel

    def __str__(self):
        return str(self.cell_type)


class FireSimFueledEngine:
    '''
    The simulator engine for this fire-spread model.
    '''
    NROWS = 19
    NCOLS = 27
    
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
        new_grid[nrows // 2][ncols // 2] = CellState(ON_FIRE, cell_fuel=4)
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
                new_cell = CellState(cell_type=cur_cell.cell_type, cell_fuel=cur_cell.cell_fuel) # default is "stay the same"
                #burn_count = self.get_adjacent_fire_count((col, row))
                # 1. Determine if any cells catch on fire
                if new_cell.cell_type == CONIFERS:  # only cell type that can burn
                    burn_count = self.get_adjacent_fire_count((col, row))
                    if burn_count > 0:
                        ignite_probability = burn_count * 0.25
                        if random.random() < ignite_probability:
                            new_cell.cell_type = ON_FIRE
                # 2. Burndown (reduce fuel) for any on-fire cells, including any just ignited above.
                if new_cell.cell_type == ON_FIRE:
                    remaining_fuel = new_cell.cell_fuel - 1
                    if remaining_fuel <= 0:
                        new_cell.cell_fuel = 0
                        new_cell.cell_type = BURNT_OUT
                    else:
                        new_cell.cell_fuel = remaining_fuel
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

    #----- developer/debug methods

    def get_current_grid_stats_text(self):
        cell_counts = self.get_current_grid_stats()
        return 'Step=' + str(self.sim_step) + 'Cell Counts: ' + ' '.join(["{0}={1}".format(CELL_TYPE_NAMES[k], v) for (k, v) in cell_counts.items()])

    def print_current_grid(self):
        '''Prints an ascii dump of the current grid to stdout.'''
        for row in range(self.sgg.get_cell_rows()):
            for col in range(self.sgg.get_cell_cols()):
                sep = ' ' if col > 0 else ''
                print("{0}{1}".format(sep, self.grid[row][col]), end='')
            print()
