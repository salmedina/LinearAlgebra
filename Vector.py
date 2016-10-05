from __future__ import division
from math import acos, pi

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __len__(self):
        return len(self.coordinates)

    def __add__(self, other):
        return Vector([x+y for x,y in zip(self.coordinates, other.coordinates)])

    def __radd__(self, other):
        return Vector([x+y for x,y in zip(self.coordinates, other.coordinates)])

    def __iadd__(self, other):
        self.coordinates = [x+y for x,y in zip(self.coordinates, other.coordinates)]

    def __sub__(self, other):
        return Vector([x-y for x,y in zip(self.coordinates, other.coordinates)])

    def __isub__(self, other):
        self.coordinates = [x-y for x,y in zip(self.coordinates, other.coordinates)]

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Vector([x*other for x in self.coordinates])
        elif type(other) == Vector:
            return sum([x*y for x,y in zip(self.coordinates, other.coordinates)])

    def __rmul__(self, other):
        if type(other) in [int, float]:
            return Vector([x*other for x in self.coordinates])
        elif type(other) == Vector:
            return sum([x*y for x,y in zip(self.coordinates, other.coordinates)])

    def __abs__(self):
        '''Returns the magnitude of the vector'''
        return (sum([x*x for x in self.coordinates]))**(1/2)

    def unit(self):
        mag = abs(self)
        if mag == 0:
            return 0
        return (1/abs(self)) * self

    def dot(self, other):
        return self * other

    def angle(self, other):
        if type(other) is not Vector:
            raise Exception("A Vector is required to calculate the angle")
        if len(self) != len(other):
            raise Exception("A Vector with the same dimensions is required")

        return acos(self*other / (abs(self)*abs(other)))

    def is_aligned(self, other):
        if type(other) is not Vector:
            raise Exception("A Vector is required to calculate the angle")
        return ( self.angle(other) == 0 )

    def is_opposite(self, other):
        if type(other) is not Vector:
            raise Exception("A Vector is required to calculate the angle")
        return ( self.angle(other) == pi)

    def is_orthogonal(self, other):
        if type(other) is not Vector:
            raise Exception("A Vector is required to calculate the angle")
        return (self * other) == 0



v1 = Vector([-0.221,7.437])
v2 = Vector([8.813,-1.331,-6.247])
v3 = Vector([5.581, -2.136])
v4 = Vector([1.996, 3.108, -4.554])

v5 = Vector([1,2,-1])
v6 = Vector([3,1,0])

print v5.angle(v6)


