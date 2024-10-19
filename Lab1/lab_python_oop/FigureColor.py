class FigureColor:
    """description of figure's color class"""

    def __init__(self, name):
        self.__color = name    

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_name):
        self.__color = new_name

    def __repr__(self):
        return self.__color