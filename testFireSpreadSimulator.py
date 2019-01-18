import unittest

from FireSpreadSimulator import FireSpreadEngine
from FireSpreadSimulator import BARE_GROUND

class TestFireSpreadEngine(unittest.TestCase):

    def test_create_FireSpreadEngine(self):
        '''Checks whether a FireSpreadEngine object gets created correctly.'''
        sim_engine = FireSpreadEngine()
        # Debugging statement, uncomment if needed:
        #sim_engine.print_current_grid()

        # The following assertions assume a specific, hardwired simulator configuration.
        # They will fail -- must be updated -- if the simulation configuration changes.
        cols = sim_engine.sgg.get_cell_cols()
        rows = sim_engine.sgg.get_cell_rows()
        self.assertEquals(cols, 21, "cols")
        self.assertEquals(rows, 17, "rows")

        # The border cells of the simulation grid should be type BARE_GROUND
        expect = BARE_GROUND
        for row in range(rows):
            for col in range(cols):
                if row == 0 or row == (rows-1):
                    actual = sim_engine.grid[row][col].cell_type
                    self.assertEquals(actual, expect, 'col={0} row={1}'.format(col, row))
                elif col == 0 or col == (cols-1):
                    actual = sim_engine.grid[row][col].cell_type
                    self.assertEquals(actual, expect, 'col={0} row={1}'.format(col, row))


if __name__ == '__main__':
    unittest.main()