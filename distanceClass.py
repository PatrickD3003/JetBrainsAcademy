import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, another_point):
        self.another_point = another_point
        return math.sqrt(pow(self.x - self.another_point.x, 2) + pow(self.y - self.another_point.y, 2))

p1 = Point(1.5, 1)
p2 = Point(1.5, 2)

print(p1.dist(p2))