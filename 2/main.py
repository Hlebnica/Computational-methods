# Вариант 2
# Найти все корни уравнения
# x^4 - 10001.01 x^3 - 9800.01 x^2 - 999901 х + 10000 = 0

# x^0 = 0.001
# x^1 = 0.011

from sympy import diff, sqrt
from sympy.abc import x


def kantorovich_check(func, _x, _x0):
    b = 1 / func.subs(_x, _x0)
    n = func.subs(_x, _x0) / diff(func, _x).subs(_x, _x0)
    k = diff(func, _x, 2).subs(_x, _x0)
    h = b * n * k

    return h <= 0.5 and (1 - sqrt(1 - 2 * h)) * n / h <= 0.5


uraven = x ** 4 - 10001.01 * x ** 3 - 9800.01 * x ** 2 - 999901 * x + 10000
print(kantorovich_check(uraven, x, 0.011))
