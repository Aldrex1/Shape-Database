import math

#Global ID value for the shapes
id_g = 1

class Shape:
    #Shape constructor
    def __init__(self):
        global id_g
        self.id = id_g
        id_g += 1

    #Print function. It checks the class name of the class and prints the correct output accordingly
    def print(self):
        classname = type(self).__name__
        if classname == "Shape":
            print(str(self.id) + ": " + classname + ", perimeter: undefined, area: undefined")
        elif classname == "Circle":
            print(str(self.id) + ": " + classname + ", perimeter: " + str(self.perimeter()) + ", area: " + str(self.area()))
        elif classname == "Ellipse":
            print(str(self.id) + ": " + classname + ", perimeter: undefined, area: " + str(self.area()) + ", linear eccentricity: " + str(self.eccentricity()))
        elif classname == "Rhombus":
            print(str(self.id) + ": " + classname + ", perimeter: "+ str(self.perimeter()) +", area: " + str(self.area()) + ", in-radius: " + str(self.inradius()))

    #Perimeter method
    def perimeter(self):
        return
    #Area method
    def area(self):
        return

#Circle subclass
class Circle(Shape):

    #Class constructor
    def __init__(self, r):
        self.radius = r
        super().__init__()

    #Overriden perimeter method
    def perimeter(self):
        peri = math.pi * self.radius * 2
        return peri

    #Overriden area method
    def area(self):
        a = self.radius * self.radius * math.pi
        return a

#Ellipse subclass
class Ellipse(Shape):

    #Class constructor
    def __init__(self, a, b):
        if a > b:
            self.semi_major = a
            self.semi_minor = b
        if a < b:
            self.semi_major = b
            self.semi_minor = a
        super().__init__()

    #Overriden area method
    def area(self):
        a = math.pi * self.semi_major * self.semi_minor
        return a

    #Eccentricity method
    def eccentricity(self):
        c = math.sqrt(self.semi_major ** 2 - self.semi_minor ** 2)
        return c

#Rhombus subclass
class Rhombus(Shape):

    #Class constructor
    def __init__(self, a, b):
        self.first_diagonal = a
        self.second_diagonal = b
        super().__init__()

    #side method
    def side(self):
        a = math.sqrt(self.first_diagonal**2 + self.second_diagonal**2) / 2
        return a

    #Overriden perimeter method
    def perimeter(self):
        p = 4 * self.side()
        return p

    #Overriden area method
    def area(self):
        a = self.first_diagonal * self.second_diagonal / 2
        return a

    #Inradius method
    def inradius(self):
        r = (self.first_diagonal * self.second_diagonal) / (2 * math.sqrt(self.first_diagonal**2 + self.second_diagonal**2))
        return r
