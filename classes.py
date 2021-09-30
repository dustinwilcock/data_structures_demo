'''
Data Structure Demo - Classes
Author: Bro. Wilcock
'''
import math

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "("+ str(self.x) +","+ str(self.y) +")"

class Line:
    def __init__(self, pt1: Point, pt2: Point):
        self.pt1 = pt1
        self.pt2 = pt2

    def getLength(self):
        # right triangle a*a + b*b = c*c, therefore c = sqrt(a*a + b*b)
        a = self.pt1.x - self.pt2.x
        b = self.pt1.y - self.pt2.y
        return math.sqrt(a*a + b*b)

class Triangle:
    def __init__(self, pt1: Point, pt2: Point, pt3):
        self.pt1 = pt1
        self.pt2 = pt2
        self.pt3 = pt3

    def getArea(self):
        # A = 1/2 |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|
        return 0.5 * abs(self.pt1.x*(self.pt2.y-self.pt3.y) + 
                         self.pt2.x*(self.pt3.y-self.pt1.y) + 
                         self.pt3.x*(self.pt1.y-self.pt2.y))

def main():
    # named tuples to store 2 points (1,0) and (2,3)
    pt1 = Point(1,0)
    pt2 = Point(2,3)
    pt3 = Point(4,5)

    #call function to get length of line segment between 2 points
    line = Line(pt1, pt2)
    print(f"The length of the line segement between points {pt1} and {pt2} is {line.getLength()}")

    #call function to get area defined by 3 points
    triangle = Triangle(pt1, pt2, pt3)
    print(f"The area of the triangle formed with points {pt1}, {pt2} and {pt3} is {triangle.getArea()}")

if __name__ == "__main__":
    main() 