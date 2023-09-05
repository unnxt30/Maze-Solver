from cell import *
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._win = win

        self._create_cells()

    def _create_cells(self):
        for i in range(self._num_cols):
            column_field = []
            for j in range(self._num_rows):
                column_field.append(Cell(self._win))
            self._cells.append(column_field)
        
        for m in range(self._num_cols): 
            for n in range(self._num_rows):
                self._draw_cell(m,n)

    def _draw_cell(self, i, j):
        if self._win is None:
            return

        x1_posn = self._x1 + i*self._cell_size_x
        y1_posn = self._y1 + j*self._cell_size_y
        x2_posn = x1_posn + self._cell_size_x
        y2_posn = y1_posn + self._cell_size_y

        self._cells[i][j].draw(x1_posn, y1_posn, x2_posn, y2_posn)
        self._animate()

    def _animate(self):
        if self._win is None:
            return

        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_UW = False
        self._draw_cell(0,0)

        self._cells[self._num_cols-1][self._num_rows-1].has_BW = False
        self._draw_cell(self._num_cols-1, self._num_rows-1)





