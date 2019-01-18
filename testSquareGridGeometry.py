import unittest
from SquareGridGeometry import SquareGridGeometry

class TestSquareGridGeometry(unittest.TestCase):
    '''
    Tests SquareGridGeometry methods.
    '''
    def setUp(self):
        # Object construction is implictly tested by creating an instance
        # That other methods will use for testing.
        self.sgg = SquareGridGeometry(cell_rows=11, cell_cols=17, cell_width=32)

    def test_get_cell_width(self):
        self.assertEqual(self.sgg.get_cell_width(), 32)

    def test_get_cell_cols(self):
        self.assertEqual(self.sgg.get_cell_cols(), 17)

    def test_get_cell_rows(self):
        self.assertEqual(self.sgg.get_cell_rows(), 11)

    def test_is_on_grid(self):
        ncols = self.sgg.get_cell_cols()
        nrows = self.sgg.get_cell_rows()
        on_location = (ncols // 2, nrows // 2)
        self.assertTrue(self.sgg.is_on_grid(on_location))
        off_location = (-ncols, -nrows)
        self.assertFalse(self.sgg.is_on_grid(off_location))

    def test_get_adjacent_cell(self):
        # test relative to upper-left corner cell of grid
        expect = [(0,-1), (1,0), (0,1), (-1,0)]
        actual = [self.sgg.get_adjacent_cell((0,0), d) for d in range(4)]
        self.assertEqual(actual, expect, "adjacent to (0,0")
        # might as well test is_on_grid while we're at it:
        expect_on_grid = [False, True, True, False]
        actual_on_grid = [self.sgg.is_on_grid(icell) for icell in actual]
        self.assertEqual(actual_on_grid, expect_on_grid, "adjacent on-grid checks")


if __name__ == '__main__':
    unittest.main()
