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
