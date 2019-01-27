import unittest

from FireSimEngine import FireSimEngine
from FireSimEngine import BARE_GROUND
from FireSimEngine import ON_FIRE

class TestFireSpreadEngine(unittest.TestCase):

    def test_create_FireSpreadEngine(self):
        '''Checks whether a FireSpreadEngine object gets created correctly.'''
        fse = FireSimEngine()
        # Debugging statement, uncomment if needed:
        #fse.print_current_grid()

        # The following assertions assume a specific, hardwired simulator configuration.
        # They will fail -- must be updated -- if the simulation configuration changes.
        cols = fse.sgg.get_cell_cols()
        rows = fse.sgg.get_cell_rows()
        self.assertEquals(cols, FireSimEngine.NCOLS, "cols")
        self.assertEquals(rows, FireSimEngine.NROWS, "rows")

        # The border cells of the simulation grid should be type BARE_GROUND
        expect = BARE_GROUND
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == (rows-1):
                    actual = fse.grid[row][col].cell_type
                    self.assertEquals(actual, expect, 'col={0} row={1}'.format(col, row))
                elif col == 0 or col == (cols-1):
                    actual = fse.grid[row][col].cell_type
                    self.assertEquals(actual, expect, 'col={0} row={1}'.format(col, row))

    def test_get_adjacent_fire_count(self):
        fse = FireSimEngine()
        # Warning!
        # This code assumes "white box" knowledge of FireSimEngine and is implementation-dependent.
        print("Center Test")
        xc = fse.sgg.get_cell_cols() // 2
        yc = fse.sgg.get_cell_rows() // 2
        fse.grid[yc][xc].cell_type = ON_FIRE
        expect = 0
        actual = fse.get_adjacent_fire_count((xc, yc))
        self.assertEquals(actual, expect, 'center cell, no adjacent fire')
        # Surround center cell with fire: result should == 4
        # because corner-adjacent cells and center cell itself do not count
        for x, y in [(xc-1,yc-1), (xc,yc-1), (xc+1, yc-1), (xc-1,yc), (xc+1,yc), (xc-1,yc+1), (xc,yc+1), (xc+1,yc+1)]:
            fse.grid[y][x].cell_type = ON_FIRE
        expect = 4
        actual = fse.get_adjacent_fire_count((xc, yc))
        self.assertEquals(actual, expect, 'center cell, all adjacent fire')
        # Surround upper-left cornder cell (0,0) with fire: result should == 2
        # because only 2 side-adjacent cells on-grid.
        print("ULC Test")
        for x, y, in [(1,0), (1,1), (0,1)]:
            fse.grid[y][x].cell_type = ON_FIRE
        expect = 2
        actual = fse.get_adjacent_fire_count((0, 0))
        self.assertEquals(actual, expect, 'upper-left corner cell, all adjacent fire')
        # Surround lower-right corner cell (NCOLS-1, NROWS-1) with fire: result should == 2
        # because only 2 side-adjacent cells on-grid.
        print("LRC Test")
        xlr = fse.sgg.get_cell_cols() - 1
        ylr = fse.sgg.get_cell_rows() - 1
        for x, y, in [(xlr-1,ylr-1), (xlr,ylr-1), (xlr-1,ylr)]:
            fse.grid[y][x].cell_type = ON_FIRE
        expect = 2
        actual = fse.get_adjacent_fire_count((xlr, ylr))
        self.assertEquals(actual, expect, 'lower-right corner cell, all adjacent fire')


if __name__ == '__main__':
    unittest.main()