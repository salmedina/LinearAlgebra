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

    def project_parallel(self, other):
        if type(other) is not Vector:
            raise Exception("A Vector is required for projection")

        u_other = other.unit()
        return (self*u_other)*u_other

    def project_orthogonal(self, other):
        if type(other) is not Vector:
            raise Exception("A Vector is required for projection")

        para_proj = self.project_parallel(other)
        return self-para_proj


v1 = Vector([3.039, 1.879])
b1 = Vector([0.825, 2.036])

print v1.project_parallel(b1)


v2 = Vector([-9.88, -3.264, -8.159])
b2 = Vector([-2.155, -9.353, -9.473])
print v2.project_orthogonal(b2)

v3 = Vector([3.009, -6.172, 3.692, -2.51])
b3 = Vector([6.404, -9.144, 2.759, 8.718])
print v3.project_parallel(b3)
print v3.project_orthogonal(b3)