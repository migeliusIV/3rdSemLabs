from lab_python_oop import Rectangle
from lab_python_oop import Box
from lab_python_oop import Cyrcle
import matplotlib.pyplot as plt


def main():
    rect = Rectangle.Rectangle(13, 13, "blue")
    print(rect)

    b = Box.Box(10, "Red")
    print(b)

    c = Cyrcle.Cyrcle(5, "Green")
    print(c)

    # Enviroment
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Easy method")
    plt.show()


if __name__ == "__main__":
    main()
