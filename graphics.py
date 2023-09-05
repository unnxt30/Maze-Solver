from tkinter import Tk, BOTH, Canvas

class Window:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.__root_widget = Tk()
        self.__root_widget.title("Maze-Solver")
        self.canvas = Canvas(self.__root_widget, height = height, width= width)
        self.canvas.pack()
        self.__running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def draw_move(self, cell, undo = False):
        return
        

class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:

    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = fill_color, width = 2)
        canvas.pack(fill = BOTH, expand = 1) 