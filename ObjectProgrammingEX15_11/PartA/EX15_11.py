class Point:
    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    def MidPoint(self, target):  # target : CLASS
        midX = (self.x + target.x) / 2
        midY = (self.y + target.y) / 2
        return Point(midX, midY)
    def distanceFromPoint(self, otherP):
        dx = otherP.x - self.x
        dy = otherP.y - self.y
        return ((dx ** 2) + (dy ** 2)) ** 0.5
    def reflect_x(self):
        return Point(self.x, - self.y)
    def slope_from_origin(self):
        if self.x == 0:
            return 0
        else:
            slope = self.y / self.x
            return slope
    def get_line_to(self, otherP):
        a = (otherP.y - self.y) / (otherP.x - self.x)
        b = self.y - self.x * a
        return Point(round(a, 2), round(b, 2))
    def move(self, dx, dy):
        NewX = self.x + dx
        NewY = self.y + dy
        return Point(NewX, NewY)

    def getCircle(self, p2, p3):
        p1 = self
        x21 = p2.x - p1.x
        y21 = p2.y - p1.y
        x32 = p3.x - p2.x
        y32 = p3.y - p2.y
        # three colinear
        if (x21 * y32 - x32 * y21 == 0):
            return None
        xy21 = p2.x * p2.x - p1.x * p1.x + p2.y * p2.y - p1.y * p1.y
        xy32 = p3.x * p3.x - p2.x * p2.x + p3.y * p3.y - p2.y * p2.y
        y0 = (x32 * xy21 - x21 * xy32) / 2 * (y21 * x32 - y32 * x21)
        x0 = (xy21 - 2 * y0 * y21) / (2.0 * x21)
        R = ((p1.x - x0) ** 2 + (p1.y - y0) ** 2) ** 0.5
        return round(x0, 2), round(y0, 2), round(R, 2)

p = Point(3, 3)
q = Point(6, 7)
o = Point(0, 0)

print('Xq :', q.getX())
print('Yq :', q.getY())
print('Distance from origin to q:', q.distanceFromOrigin())
print('Point p : ',p)
print('Midpoint between p and q :',q.MidPoint(p))

print()

print('Question 1')
print('Distance from point p to q :', p.distanceFromPoint(q))

print()

print('Question 2')
print('the x reflection of p :', p.reflect_x())

print()

print('Question 3')
print('the slope of p from the origin :', p.slope_from_origin())

print()

print('Question 4')
print('The (a, b) of y = ax + b is :', p.get_line_to(q))

print()

print('Question 5')
print('The new point :', p.move(2, 3))

print()

print('Question 6')
print(o.getCircle(p, q))



