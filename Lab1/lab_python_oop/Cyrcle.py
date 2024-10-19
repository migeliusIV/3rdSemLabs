import math
from lab_python_oop import FigureColor
from lab_python_oop import Shape

class Cyrcle(Shape.Shape):
    """description of class"""
    
    type = "Cyrcle"
        
    def __init__(self, r, col = "white"):
        self.r = r
        self.col = col
    
    def square(self): return (self.r ** 2) * math.pi

    def __repr__(self):
        return ('{} R = {}, color = {}. Square = {}'.format(
            self.print_type(),
            self.r,
            self.col,
            self.square())
        )