from lab_python_oop import Rectangle
from lab_python_oop import Box
from lab_python_oop import Cyrcle

def main():
    rect = Rectangle.Rectangle(13, 15) 
    print(rect)
    
    b = Box.Box(10)
    print(b)
    
    c = Cyrcle.Cyrcle(5)
    print(c)

if __name__ == "__main__":
    main()