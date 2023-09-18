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
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visted()
        

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
        # self._cells[i][j].visited = True
        # while True:
        #     toVisit = []
        #     possible = 0

        #     if i > 0 and not self._cells[i-1][j].visited:
        #         toVisit.append((i-1, j))
        #         possible += 1

        #     if i < self._num_cols - 1 and not self._cells[i+1][j]:
        #         toVisit.append((i+1,j))
        #         possible+=1

        #     if j > 0 and not self._cells[i][j-1].visited:
        #             toVisit.append((i,j-1))
        #             possible += 1
            
        #     if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
        #         toVisit.append((i,j+1))
        #         possible += 1

            
        #     if possible == 0:
        #         self._draw_cell(i,j)
        #         return

        #     random_index = random.randrange(possible)
        #     next_index = toVisit[random_index]

        #     if next_index[0] == i+1:
        #         self._cells[i][j].has_RW = False
        #         self._cells[i+1][j].has_LW = False
            
        #     if next_index[0] == i-1:
        #         self._cells[i-1][j].has_RW = False
        #         self._cells[i][j].has_LW = False
            
        #     if next_index[1] == j+1:
        #         self._cells[i][j+1].has_UW = False
        #         self._cells[i][j].has_BW = False
            
        #     if next_index[1] == j-1:
        #         self._cells[i][j-1].has_BW = False
        #         self._cells[i][j].has_UW = False
            
        #     self._break_walls_r(next_index[0], next_index[1])
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            possible_direction_indexes = 0

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
                possible_direction_indexes += 1
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
                possible_direction_indexes += 1
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
                possible_direction_indexes += 1
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
                possible_direction_indexes += 1

            # if there is nowhere to go from here
            # just break out
            if possible_direction_indexes == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(possible_direction_indexes)
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_RW = False
                self._cells[i + 1][j].has_LW = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_LW = False
                self._cells[i - 1][j].has_RW = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_BW = False
                self._cells[i][j + 1].has_UW = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_UW = False
                self._cells[i][j - 1].has_BW = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])

    
    def _reset_cells_visted(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def _solve_r(self, i, j):
        
        self._animate()

        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        # up
        if (j>0 and (not self._cells[i][j-1].visited) and (not self._cells[i][j].has_UW)):

            self._cells[i][j].draw_move(self._cells[i][j-1])

            if self._solve_r(i, j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1],True)    
            
        if (j < self._num_rows - 1 and (not self._cells[i][j+1].visited )and (not self._cells[i][j].has_BW)):

            self._cells[i][j].draw_move(self._cells[i][j+1])

            if self._solve_r(i, j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1],True)
        
        if (i>0 and (not self._cells[i-1][j].visited) and (not self._cells[i][j].has_LW)):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j],True)
                
            # right
        if (i< self._num_cols - 1 and (not self._cells[i+1][j].visited) and (not self._cells[i][j].has_RW)):

            self._cells[i][j].draw_move(self._cells[i+1][j])
            
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j],True)

        return False

    def solve(self):
        return self._solve_r(0,0)