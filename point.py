import random

class Point:
    def _init_(self, x, y):
        """
        Initialize a Point object
        :param x:  the x position on the axis
        :param y: the y position on the axis
        """
        self.x = x # define x attribute via self.x
        self.y = y # and assign the value x to it

    def _str_(self):
        """
        Magic method that is called when we try to print an instance of the Point object
        :return: <x, y>
        """
        return f"<{self.x}, {self.y}>"

    def _repr_(self):
        return self._str_() # use the same way of printing as str

    def distance_orig(self):
        return (self.x*2 + self.y2)*0.5 # square root of the sum of x and y squared

    def _gt_(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance > other_distance

    def _eq_(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance

if _name_ == "_main_":
    # now we need to instantiate it!
    p = Point(1,2) # p is an instance of 1 and 2
    print(f"p.x = {p.x} and p.y = {p.y}")
    p.x = 20
    print(f"p.x = {p.x} and p.y = {p.y}")
    print(p)
    # create a list of 5 random points
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10, 10), # x value
                            random.randint(-10, 10))) # y value
    print("I got this 5 random points:")
    print(points)
    p = Point(3, 4)
    print(p.distance_orig()) # expect 5 answer
    p2 = Point(1,1)
    print(f"I am comparing p > p2: {p > p2}") # I expect to have True
    print("the sorted list of point is:")
    points.sort()
    print(points)