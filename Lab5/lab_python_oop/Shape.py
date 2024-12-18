import abc


class Shape(abc.ABC):
    """description of abstract class"""

    @classmethod
    def print_type(arg):
        return arg.type

    @abc.abstractmethod
    def square(self):
        pass
