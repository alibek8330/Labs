class Shape:
  class Rectangle:
    def __init__(self, length, width):
      self.length = int
      self.width = int
      self.length = length
      self.width = width
    def area(self):
      print(self.length * self.width)
      
l = int(input())
w = int(input())
result = Shape.Rectangle(l, w)
result.area()