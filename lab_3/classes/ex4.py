class Point:
  def __init__(self, x0, y0, x, y):
    self.x0 = x0
    self.y0 = y0
    self.x = x
    self.y = y
  # def move(self):

  def show(self):
    print(self.x, self.y)
    
  def dist(self):
    print(float(((self.x - self.x0)**2 + (self.y - self.y0)**2)**0.5))
    
x0 = int(input())
y0 = int(input())
x = int(input())
y = int(input())
result = Point(x0, y0, x, y)
result.show()
result.dist()
