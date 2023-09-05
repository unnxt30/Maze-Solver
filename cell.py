from graphics import Line, Point

class Cell:
    
    def __init__(self, win=None):
        self._x1 = None 
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_LW = True
        self.has_UW = True
        self.has_BW = True
        self.has_RW = True
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1 
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        if self.has_LW:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            left_wall = Line(p1, p2)
            self._win.draw_line(left_wall, "black")
        else:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x1, self._y2)
            left_wall = Line(p1, p2)
            self._win.draw_line(left_wall, "#e0dcdc")
        


        if self.has_RW:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2 , self._y2)
            right_wall = Line(p1, p2)
            self._win.draw_line(right_wall, "black")

        else:
            p1 = Point(self._x2, self._y1)
            p2 = Point(self._x2 , self._y2)
            right_wall = Line(p1, p2)
            self._win.draw_line(right_wall, "#e0dcdc")

        if self.has_UW:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            upper_wall = Line(p1, p2)
            self._win.draw_line(upper_wall, "black")
        else:
            p1 = Point(self._x1, self._y1)
            p2 = Point(self._x2, self._y1)
            upper_wall = Line(p1, p2)
            self._win.draw_line(upper_wall, "#e0dcdc")

        if self.has_BW:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2 , self._y2)
            bottom_wall = Line(p1, p2)
            self._win.draw_line(bottom_wall, "black")

        else:
            p1 = Point(self._x1, self._y2)
            p2 = Point(self._x2 , self._y2)
            bottom_wall = Line(p1, p2)
            self._win.draw_line(bottom_wall, "#e0dcdc")

    def draw_move(self, to_cell, undo = False):
        if self._win is None:
            return
        x_mid = (self._x1 + self._x2) / 2
        y_mid = (self._y1 + self._y2) / 2

        to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        to_y_mid = (to_cell._y1 + to_cell._y2) / 2

        fill_color = "red"
        if undo:
            fill_color = "gray"

        # moving left
        if (not self.has_LW or not self.has_UW or not self.has_BW or not self.has_RW):
            line = Line(Point(x_mid, y_mid), Point(to_x_mid, to_y_mid))
            self._win.draw_line(line, fill_color)

        # moving left
        # if self._x1 > to_cell._x1:
        #     line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
        #     self._win.draw_line(line, fill_color)
        #     line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
        #     self._win.draw_line(line, fill_color)

        # # moving right
        # elif self._x1 < to_cell._x1:
        #     line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
        #     self._win.draw_line(line, fill_color)
        #     line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
        #     self._win.draw_line(line, fill_color)

        # # moving up
        # elif self._y1 > to_cell._y1:
        #     line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
        #     self._win.draw_line(line, fill_color)
        #     line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
        #     self._win.draw_line(line, fill_color)

        # # moving down
        # elif self._y1 < to_cell._y1:
        #     line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
        #     self._win.draw_line(line, fill_color)
        #     line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
        #     self._win.draw_line(line, fill_color)