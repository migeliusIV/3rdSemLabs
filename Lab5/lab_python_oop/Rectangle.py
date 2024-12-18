from lab_python_oop import Shape
from lab_python_oop import FigureColor


class Rectangle(Shape.Shape):
    """description of main class"""

    type = "Rectangle"

    def __init__(self, width, height, col="white"):
        self.width = width
        self.height = height
        self.col = FigureColor.FigureColor(col)

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return "{} Width = {}, height = {}, color = {}. Square = {}".format(
            self.print_type(), self.width, self.height, self.col, self.square()
        )
