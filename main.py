'''
from fractions import Fraction

try:
    class Calculator:
        def add(self, a, b):
            return a + b

        def subtract(self, a, b):
            return a - b

        def miltiply(self, a, b):
            return a * b


except ZeroDivisionError:
    print("на ноль делить нельзя")


class AdvancedCalculator(Calculator):
    def power(self, a, b):
        return a ** b

    def sqrt(self, a):
        import math
        return math.sqrt(a)

    def divide(self, a, b):
        return Fraction(a / b)

calc = Calculator()
print(calc.add(5, 3))
adv_calc = AdvancedCalculator()
print(calc.divide(3, 4))
print(adv_calc.power(2, 3))
print(adv_calc.sqrt(16))
'''
'''
from abc import ABC, abstractmethod
class BaseCalculator(ABC):
    @abstractmethod
    def rez(self):
        pass

class SimpleCalculator(BaseCalculator):
    def add(self, a, b):
        self.a = a
        self.b = b
        def rez(self):
            return "result =", a + b

    def subtract(self, a, b):
        self.a = a
        self.b = b
        def rez(self):
            return "result =", a - b

calc = SimpleCalculator()
calc.add(5, 3)
'''

from abc import ABC, abstractmethod
class TeamFortress2(ABC):
    @abstractmethod
    def points(self):
        pass

class pyro(TeamFortress2):
    def __init__(self, points):
        self.points = points

    def points(self):
        print("i have", self.points, "points")

class sniper(TeamFortress2):
    def __init__(self, points, headShots):
        self.points = points
        self.headShots = headShots

    def points(self):
        print("i have", self.points, " and ", self.headShots, "headShots")

Ilya = pyro(150)
Ilya.points()
Denis = sniper(200, 100)
Denis.points()
