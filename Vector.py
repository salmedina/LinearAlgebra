from __future__ import division
from math import acos, pi, sqrt
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
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
        if type(other) in [int, float, Decimal]:
            '''Scalar multiplication'''
            return Vector([x*Decimal(other) for x in self.coordinates])
        elif type(other) == Vector:
            '''Vector multiplication'''
            return sum([x*y for x,y in zip(self.coordinates, other.coordinates)])

    def __rmul__(self, other):
        if type(other) in [int, float, Decimal]:
            '''Scalar multiplication'''
            return Vector([x*Decimal(other) for x in self.coordinates])
        elif type(other) == Vector:
            '''Vector multiplication'''
            return sum([x*y for x,y in zip(self.coordinates, other.coordinates)])

    def __abs__(self):
        '''Returns the magnitude of the vector'''

        return (sum([x*x for x in self.coordinates]))**(Decimal(0.5))

    def unit(self):
        mag = abs(self)
        if mag == 0:
            return 0
        return (Decimal(1.0)/mag) * self

    def dot(self, other):
        return self * other

    def normalized(self):
        return self.unit()

    def angle(self, other, deg=False):
        if type(other) is not Vector:
            raise Exception("A Vector is required to calculate the angle")
        if len(self) != len(other):
            raise Exception("A Vector with the same dimensions is required")

        u1 = self.unit()
        u2 = other.unit()

        angle_rad = Decimal(acos(u1*u2))
        if deg:
            return angle_rad * Decimal(180.0/pi)
        return angle_rad

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


v1 = Vector([7.887, 4.138])
v2 = Vector([-8.802, 6.776])

v3 = Vector([-5.955, -4.904, -1.874])
v4 = Vector([-4.496, -8.755, 7.103])

v5 = Vector([3.183, -7.627])
v6 = Vector([-2.668, 5.319])

v7 = Vector([7.35, 0.221, 5.188])
v8 = Vector([2.751, 8.259, 3.985])

print v1*v2
print v3*v4

print v5.angle(v6)
print v7.angle(v8, deg=True)


