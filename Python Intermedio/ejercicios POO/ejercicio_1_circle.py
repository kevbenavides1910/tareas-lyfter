import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


radius = float(input("Enter the radius: "))
c = Circle(radius)
print(f"Radius: {c.radius}")
print(f"Area: {c.get_area():.2f}")
