"""


Class inheritance practice using common shapes which build on a base class called shapes.
Define subclasses using two dimensional shapes (circle, square, rectangle, triangle, parallelogram)

Using the base class Shape, define a subclass for circle.
"""
import math


class Shape:
    """
    The base class Shape defines some common methods that should be implemented in
    all subclasses. Only the __init__, __str__, __add__, and __sub__ methods need to
    be implemented in the sublasses.
    """


    def __init__(self):
        """
        Define the init method to accept dimensional arguments which will describe the
        shape.
        """
        pass

    @property
    def area(self):
        """
        Returns the area of the shape
        """
        raise NotImplementedError

    @property
    def circumference(self):
        """
        Returns the circumference of the shape
        """
        raise NotImplementedError


    # Comparison operators. For equality and inequality, we include a check of whether
    # the object is of the same class

    def __eq__(self, other):
        """
        Equality test between two shapes. For a shape to be equal, it must be of the same
        type and have the same dimensions. Use the built-in function isinstance to test
        if an object is of certain class.
        """
        result = False
        if isinstance(other, Shape) and (self.area == other.area):
            return True
        else:
            return False

    def __ne__(self, other):
        """
        The negation of __eq__()
        """
        return not self.__eq__(other)


    def __ge__(self, other):
        """
        Returns True if the area this (self) shape is greater than the area of other
        """
        result = False
        if  isinstance(other, Shape) and (self.area >= other.area):
            result = True
        return result


    def __le__(self, other):
        """
        Returns True if the area of this (self) shape is less than or equal to the area of
        other
        """
        result = False
        if isinstance(other, Shape) and (self.area <= other.area):
            result = True
        return result


    def __gt__(self, other):
        """
        The negation of __le__()
        """
        result = False
        if isinstance(other, Shape):
            result = not self.__le__(other)
        return result


    def __lt__(self, other):
        """
        The negation of __ge__()
        """
        result = False
        if isinstance(other, Shape):
            result = not self.__ge__(other)
        return result


# Math on shapes, build new shapes by combining the area of two different shapes

    def __add__(self, other):
        """
        Add two shapes together (lhs + rhs). The summation should be of the same subclass
        as the lhs with an area equal to the combined area of lhs and rhs.
        As an example: new_circle = circle + square, creates a new circle by increasing
        the radius such that the area equals circle.area() + square.area().
        """
        raise NotImplementedError


    def __sub__(self, other):
        """
        Subtracts other shape from this shape (lhs - rhs). The result should be of the
        same subclass as the lhs with and area equal to the area of lhs less the area of
        rhs. If the resulting area would be zero or less than None is returned.
        """
        raise NotImplementedError


    def __str__(self):
        """
        Returns a string representation of the shape in the form of
        "shape[dimensions ..., area, circumference]"
        """
        return "shape[]"

    def draw(self):
       print("{:6.1f}{}".format(self.area,self))

#********************************************************

class Circle(Shape):

    def __init__(self, radius):
        """
        A circle is defined by its radius
        """
        self.radius = radius

    @property
    def area(self):
        """
        Returns the area of the shape
        """
        return math.pi * math.pow(self.radius, 2)

    @property
    def circumference(self):
        """
        Returns the circumference of the shape
        """
        return math.pi * self.radius * 2

# Math on shapes, build new shapes by combining the area of two different shapes

    def __add__(self, other):
        """
        Creates a new instance of circle by increasing the radius such that the area
        equals circle.area() + other.area().
        """
        new_area = self.area + other.area
        new_radius = math.sqrt(new_area/math.pi)
        new_circle = Circle(new_radius)

        return new_circle



    def __sub__(self, other):
        """
        Subtracts other shape from this shape (lhs - rhs).  If the resulting area would
         be zero or less, than None is return
        """
        new_circle = None
        new_area = self.area - other.area
        if new_area > 0:
            new_radius = math.sqrt(new_area/math.pi)
            new_circle = Circle(new_radius)

        return new_circle


    def __str__(self):
        """
        Returns a string representation of the shape in the form of
        "shape[dimensions ..., area, circumference]"
        """
        return "circle[{:.1f}]".format(self.radius)

#***************************************************************

class Square(Shape):
    """
        A square has one dimension for the length of an egde, an area = len^2, and
        a circumference of  circumference = 4 * len
    """

    def __init__(self):
        #FIXME
        pass

    @property
    def area(self):
        """
        Returns the area of the shape
        """
        return NotImplemented

    @property
    def circumference(self):
        """
        Returns the circumference of the shape
        """
        return NotImplemented


    def __add__(self,other):
        #FIXME
        return NotImplemented

    def __sub__(self,other):
        #FIXME
        return NotImplemented

    def __str__():
        #FIXME
        return NotImplemented

class Isosceles(Shape):
    """
    An isosceles triangle has a base and a height where the area = (b*h)/2. The
    circumference (or perimeter) is found by first calculating the length of the side
    a = sqrt((b/2)^2 + h^2), then circumference = 2*a + b.
    """

    def __init__(self,base,height):
        self.base = base
        self.height = height

    @property
    def area(self):
        """
        Returns the area of the shape
        """
        return (self.base * self.height) / 2

    @property
    def circumference(self):
        """
        Returns the circumference of the shape
        """
        side = math.sqrt((self.base/2)**2 + self.height**2)
        return 2 * side + self.base

    def __add__(self,other):
        """
        Constrain the new isosceles to base/height = self.base/self.height (proportional to
        the lhs) with base = (height * self.base)/self.height. Given that  (base*height)/2 = self.area + other.area.
        Solve for height, then base.
        """
        area = self.area + other.area
        height = math.sqrt((2 * area * self.height)/self.base)
        base = (height * self.base)/self.height
        return isosceles(base,height)

    def __sub__(self,other):
        #FIXME
        return NotImplemented

    def __str__(self):
        return "Isosceles[{:.1f},{:.1f}]".format(self.base,self.height)

#***********************************************************************

def main():
    """
    Run some tests
    """

    shapes = []

    for radius in [1, .5, 6, 4, 3, 2, 5]:
        shapes.append(Circle(radius))

    # for edge in [1, .5, 10, 6, 4, 3, 7, 2, 9, 8, 5]:
    #     shapes.append(Square(edge))

    for base, height in [(1,1), (1,2), (2,2), (4,4)]:
        shapes.append(Isosceles(base, height))

    shapes.sort()

    #FIXME
    #ask shapes in the shapes list to draw themselves

if __name__ == "__main__":
    main()


