from cell import *
import random
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None, seed = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._cells = []
        self._win = win
        self._seed = seed

        self._create_cells()

        if seed is not None:
            random.seed(seed)
        

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


    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            toVisit = []
            possible = 0

            if i > 0 and i < self._num_cols - 1:
                
                # down cell
                if not self._cells[i+1][j].visited:
                    toVisit.append([i+1, j])
                    possible+=1

                # up cell
                if not self._cells[i-1][j].visited:
                    toVisit.append([i-1, j])
                    possible+=1

            if j > 0 and j < self._num_rows -1:

                #right cell
                if not self._cells[i][j+1].visited:
                    toVisit.append([i, j+1])
                    possible+=1

                # left cell
                if not self._cells[i][j-1].visited:
                    toVisit.append([i, j-1])
                    possible+=1

            
            if possible == 0:
                self._draw_cell(i,j)
                return

            random_index = random.randrange(possible)
            next_index = toVisit(random_index)

            if next_index[0] == i+1:
                self._cells[i][j].has_RW = False
                self._cells[i+1][j].has_LW = False
            
            if next_index[0] == i-1:
                self._cells[i-1][j].has_RW = False
                self._cells[i][j].has_LW = False
            
            if next_index[1] == j+1:
                self._cells[i][j+1].has_UW = False
                self._cells[i][j].has_BW = False
            
            if next_index[1] == j-1:
                self._cells[i][j-1].has_BW = False
                self._cells[i][j] = False
            
            self._break_walls_r(next_index[0], next_index[1])
            self._reset_cells_visited()
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in random(self._num_rows):
                self._cells[i][j].visited = False


    def solve(self):
        return self._solve_r(0,0)

    def _solve_r(self, i, j):
        
        current_cell = self._cells[i][j]
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        # up
        if (j>0):

            if self._cells[i][j-1]:
                upper_cell = self._cells[i][j-1]
                if not upper_cell.visited and (not current_cell.has_UW) and (not upper_cell.has_BW):
                    current_cell.draw_move(upper_cell)
                
                if self._solve_r(i, j-1):
                    return True
                
                else:
                    current_cell.draw_move(i,j-1,True)    
            
            # down
            if self._cells[i][j+1]:
                down_cell = self._cells[i][j+1]
                if not down_cell.visited and (not current_cell.has_BW) and (not down_cell.has_UW):
                    current_cell.draw_move(down_cell)

                if self._solve_r(i, j+1):
                    return True

                else:
                    current_cell.draw_move(i,j+1,True)
        
        if (i>0):

            # left
            if self._cells[i-1][j]:
                left_cell = self._cells[i-1][j]

                if not left_cell.visited and (not current_cell.has_LW) and (not left_cell.has_RW):
                    current_cell.draw_move(left_cell)
                
                if self._solve_r(i-1,j):
                    return True
                
                else:
                    current_cell.draw_move(i-1,j,True)
                
            # right
            if self._cells[i+1][j]:
                right_cell = self._cells[i+1][j]

                if not right_cell.visited and (not current_cell.has_RW) and (not right_cell.has_LW):
                    current_cell.draw_move(right_cell)
                
                if self._solve_r(i+1,j):
                    return True
                
                else:
                    current_cell.draw_move(i+1,j,True)


        return False


        

        
