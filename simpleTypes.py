'''
Data Structure Demo - Simple data types
Author: Brother Wilcock
'''
import math

def main():
    # store points (1,0) and (2,3) and (4,5)
    x1 = 1
    y1 = 0
    x2 = 2
    y2 = 3
    x3 = 4
    y3 = 5

    # get length of line segment between first 2 points
    print(f"The length of the line segement between points ({x1},{y1}) and ({x2},{y2}) is {getLineLength(x1, y1, x2, y2)}")

    # get area of a triangle defined by 3 points
    print(f"The area of the triangle formed with points ({x1},{y1}), ({x2},{y2}) and ({x3},{y3}) is {getTriangleArea(x1, y1, x2, y2, x3, y3)}")

def getLineLength(x1: int, y1: int, x2: int, y2: int):
    # right triangle a*a + b*b = c*c, c = sqrt(a*a + b*b)
    a = x1 - x2
    b = y1 - y2
    return math.sqrt(a*a + b*b)

def getTriangleArea(x1: int, y1: int, x2: int, y2: int, x3: int, y3: int):
    # A = 1/2 |x1(y2 − y3) + x2(y3 − y1) + x3(y1 − y2)|
    return 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))

if __name__ == "__main__":
    main() 
