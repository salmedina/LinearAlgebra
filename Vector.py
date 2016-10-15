from __future__ import division
from math import acos, pi, sqrt
from decimal import Decimal, getcontext

getcontext().prec = 30

def isclose(a, b, rel_tol=1e-03, abs_tol=1e-10):
    rel_tol = Decimal(rel_tol)
    abs_tol = Decimal(abs_tol)
    return abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)

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
        _, u = self.normalize()
        return u

    def dot(self, other):
        return self * other

    def normalize(self):
        '''
        :return:mag: magnitude of the vector
        :return:unit: unit vector
        '''
        mag = abs(self)
        if isclose(mag, 0):
            return 0, self
        return mag, (Decimal(1.0) / mag) * self

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

    def is_zero(self):
        return isclose(abs(self), Decimal(0.0))

    def is_aligned(self, other):
        if type(other) is not Vector:
            raise Exception("A Vector is required to calculate the angle")
        return isclose(self.angle(other), Decimal(0))

    def is_opposite(self, other):
        if type(other) is not Vector:
            raise Exception("A Vector is required to calculate the angle")
        return isclose( self.angle(other), Decimal(pi) )

    def is_parallel(self, other):
        '''By definition'''
        return (isclose(abs(self), Decimal(0.0)) or
                isclose(abs(other), Decimal(0.0)) or
                self.is_opposite(other) or
                self.is_aligned(other) )

    def is_orthogonal(self, other):
        if type(other) is not Vector:
            raise Exception("A Vector is required to calculate the angle")
        return isclose(self * other, Decimal(0))


v1 = Vector([-7.579, -7.88])
w1 = Vector([22.737, 23.64])

v2 = Vector([-2.029, 9.97, 4.172])
w2 = Vector([-9.231, -6.639, -7.245])

v3 = Vector([-2.328, -7.284,-1.214])
w3 = Vector([-1.821,1.072,-2.94])

v4 = Vector([2.118, 4.827])
w4 = Vector([0,0])


print v1.angle(w1)
print v1.is_parallel(w1)
print v1.is_orthogonal(w1)
print ''
print v2.angle(w2)
print v2.is_parallel(w2)
print v2.is_orthogonal(w2)
print ''
print v3.angle(w3)
print v3*w3
print v3.is_parallel(w3)
print v3.is_orthogonal(w3)
print ''
print v4.angle(w4)
print v4.is_parallel(w4)
print v4.is_orthogonal(w4)

