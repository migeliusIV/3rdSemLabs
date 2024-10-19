from lab_python_oop import Rectangle

class Box(Rectangle.Rectangle):
    """description of class"""
    
    type = "Square"
    
    def __init__(self, width, col = "white"):
        self.width = width
        self.col = col
       
    def square(self): return self.width ** 2
    
    def __repr__(self):
        return ('{} Width = {}, color = {}. Square = {}'.format(
            self.print_type(),
            self.width,
            self.col,
            self.square())
        )