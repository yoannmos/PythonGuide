import math


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vector = [self.x, self.y]

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def rotation(self, angle_degree):
        angle_radian = angle_degree * math.pi / 180
        x = int(round(self.x * math.cos(angle_radian) -
                      self.y * math.sin(angle_radian), 0))
        y = int(round(self.x * math.sin(angle_radian) +
                      self.y * math.cos(angle_radian), 0))
        return Vector(x, y)


# v = Vector(-1,0)
# print("v",v.x, v.y)
# v = v.rotation(180)
# print("vrot",v.x, v.y)
# v = v.rotation(45)
# print("vrot",v.x, v.y)
# v = v.rotation(180)
# print("vrot",v.x, v.y)
# v = v.rotation(-90)
# print("vrot",v.x, v.y)
if __name__ == "__main__":
    v = Vector(1, 3)
    v2 = Vector(2, 4)
    print(v.x)
    print(v2.y)
    v3 = v.__add__(v2)
    print(v3.vector)
    v4 = v + v2
    print(v4.vector)
    print(v4.rotation(45).vector)
