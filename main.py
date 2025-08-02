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
