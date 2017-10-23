from SquareGridGeometry import SquareGridGeometry

class TestSquareGridGeometry:
    '''
    Tests SquareGridGeometry methods.
    Object construction is implictly tested by creating an instance
    to test methods upon.
    '''
    sgg = SquareGridGeometry(cell_rows=11, cell_cols=17, cell_width=32)

    def test_get_cell_width(self):
        assert self.sgg.get_cell_width() == 32

    def test_get_cell_cols(self):
        assert self.sgg.get_cell_cols() == 17

    def test_get_cell_rows(self):
        assert self.sgg.get_cell_rows() == 11

    def test_is_on_grid(self):
        ncols = self.sgg.get_cell_cols()
        nrows = self.sgg.get_cell_rows()
        on_location = (ncols // 2, nrows // 2)
        assert self.sgg.is_on_grid(on_location)
        off_location = (-ncols, -nrows)
        assert not self.sgg.is_on_grid(off_location)
