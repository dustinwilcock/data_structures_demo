'''
Data Structure Demo - Named tuples, structs, records
Author: Bro. Wilcock
'''
import math
from typing import NamedTuple

class Point(NamedTuple):
    x: int
    y: int

class Line(NamedTuple):
    pt1: Point
    pt2: Point

class Triangle(NamedTuple):
    pt1: Point
    pt2: Point
    pt3: Point

def main():
    # store points (1,0) and (2,3) and (4,5)
    pt1 = Point(1,0)
    pt2 = Point(2,3)
    pt3 = Point(4,5)

    # get length of line segment between first 2 points
    line = Line(pt1,pt2)
    print(f"The length of the line segement between points ({pt1.x},{pt1.y}) and ({pt2.x},{pt2.y}) is {getLineLength(line)}")

    # get area of a triangle defined by 3 points
    tri = Triangle(pt1, pt2, pt3)
    print(f"The area of the triangle formed with points ({pt1.x},{pt1.y}), ({pt2.x},{pt2.y}) and ({pt3.x},{pt3.y}) is {getTriangleArea(tri)}")

def getLineLength(line: Line):
    # right triangle a*a + b*b = c*c, c = sqrt(a*a + b*b)
    a = line.pt1.x - line.pt2.x
    b = line.pt1.y - line.pt2.y
    return math.sqrt(a*a + b*b)

def getTriangleArea(tri: Triangle):
    # A = 1/2 |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|
    return 0.5 * abs(tri.pt1.x*(tri.pt2.y-tri.pt3.y) + 
                     tri.pt2.x*(tri.pt3.y-tri.pt1.y) + 
                     tri.pt3.x*(tri.pt1.y-tri.pt2.y))

if __name__ == "__main__":
    main() 
