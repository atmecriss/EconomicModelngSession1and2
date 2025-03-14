from point import Point
import random

class ColorPoint(Point):
    def _init_(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def _str_(self):
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1,2,"red")
print(p)
colors = ["red", "green", "blue", "yellow", "black", "magenta,",
          "cyan", "white", "burgundy", "periwinkle", "marsala"]
color_points = []
for i in range(10):
    color_points.append(
    ColorPoint(random.randint(-10, 10),
               random.randint(-10, 10),
               random.choice(colors)))


print(color_points)
color_points.sort()
print(color_points)