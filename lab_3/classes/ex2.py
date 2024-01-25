class Shape:
    def area(self):
        print(self.length * self.length)


class Square(Shape):
    def __init__(self, length=0):
        self.length = length

    def area(self):
        print(self.length * self.length)


fig1 = Square()
fig1.area()
