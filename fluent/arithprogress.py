"""
стр 451
"""


class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end  # None -> "бесконечный" ряд
    
    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)  # result = self.begin, приведенное к типу последующих слагаемых
        forever = self.end is None  # True если end None
        index = 0
        while forever or result < self.end:  # Этот цикл продолжается вечно или пока значение result не окажется больше или равно self.end
            yield result  # отдается текущее значение result
            index += 1
            result = self.begin + self.step * index  # вычисляется следующий потенциальный результат. Возможно, он никогда не будет отдан, потому что цикл завершится раньше


"""
from arithprogress import ArithmeticProgression
"""
ap = ArithmeticProgression(0, 1, 3)
l = list(ap)
print(l)
# [0, 1, 2]
ap = ArithmeticProgression(1, .5, 3)
l = list(ap)
print(l)
# [1.0, 1.5, 2.0, 2.0]
ap = ArithmeticProgression(0, 1/3, 1)
l = list(ap)
print(l)
# [0.0, 0.333333333333333, 0.666666666666666]
from fractions import Fraction
ap = ArithmeticProgression(0, Fraction(1, 3), 1)
l = list(ap)
print(l)
# [Fraction(0, 1), Fraction(0, 1), Fraction(0, 1)]
from decimal import Decimal
ap = ArithmeticProgression(0, Decimal('.1'), .3)
l = list(ap)
print(l)
# [Decimal('0.0'), Decimal('0.1'), Decimal('0.2')]
