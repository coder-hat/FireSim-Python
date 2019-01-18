# 2017-10-21

class SquareGridGeometry:
    '''
    Provides the dimensions and directional math for a 2-dimensional grid of cells.
    The cells are square, and storing cell width allows class to provide cell-to-pixel conversions.
    '''
    OFF_GRID_INDEX = -1
    ''' Value returned by methods to indicate location result was outside the grid dimensions -- class variable.'''

    # DIRECTION_OFFSETS indices are bound to direction as follows:
    #   0
    # 3 . 1
    #   2
    # i.e., counter-clockwise from above.
    DIRECTION_OFFSETS = [
        (0, -1), # up, north
        (1, 0), # right, east
        (0, 1), # down, south
        (-1, 0) # left, west
    ]

    def __init__(self, cell_rows=1, cell_cols=1, cell_width=1):
        self.cell_rows = cell_rows
        self.cell_cols = cell_cols
        self.cell_width = cell_width

    def get_cell_rows(self):
        '''Gets the number of rows this grid was dimensioned with.'''
        return self.cell_rows

    def get_cell_cols(self):
        '''Gets the number of columns this grid was dimensioned with.'''
        return self.cell_cols

    def get_cell_width(self):
        '''Gets the width (in pixels) of a single cell in this grid.  Cells are square.'''
        return self.cell_width

    def is_on_grid(self, cell_location):
        '''
        Returns True if the specified (x, y) cell_location
        is a valid pair coordinates for this grid's dimensions.
        Otherwise, returns False.
        '''
        x, y = cell_location
        col_check = x if x >= 0 and x < self.cell_cols else self.OFF_GRID_INDEX
        row_check = y if y >= 0 and y < self.cell_rows else self.OFF_GRID_INDEX
        return col_check != self.OFF_GRID_INDEX and row_check != self.OFF_GRID_INDEX

    def get_adjacent_cell(self, cell_location, direction):
        '''
        Returns a tuple containing the (x, y) location adjacent to the specified
        cell_location tuple in the specified direction from the cell_location.
        '''
        x = cell_location[0] + self.DIRECTION_OFFSETS[direction][0]
        y = cell_location[1] + self.DIRECTION_OFFSETS[direction][1]
        return (x, y)
