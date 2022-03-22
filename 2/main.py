# Вариант 2
# Найти все корни уравнения
# x^4 - 10001.01 x^3 - 9800.01 x^2 - 999901 х + 10000 = 0

# x0 = 0.011

from sympy import diff, sqrt
from sympy.abc import x


def kantorovich_check(func, _x, _x0):
    b = abs(1 / diff(func, _x).subs(_x, _x0))
    n = abs(func.subs(_x, _x0) / diff(func, _x).subs(_x, _x0))
    k = abs(diff(func, _x, 2).subs(_x, _x0))
    h = b * n * k

    return h <= 0.5


def newton_formula(func, _x, _x0):
    exp = 0.000001
    x_n = _x0
    max_iteration = 100
    k = 0
    while k <= max_iteration:
        k += 1
        x_n1 = x_n - func.subs(_x, x_n) / diff(func, _x).subs(_x, x_n)
        if abs(x_n1 - x_n) <= exp:
            break
        x_n = x_n1

    return x_n


def check(newton_formula_root):
    answer = abs(newton_formula_root ** 4 - 10001.01 * newton_formula_root ** 3 - \
                 9800.01 * newton_formula_root ** 2 - 999901 * newton_formula_root + 10000)

    return answer


equation = x ** 4 - 10001.01 * x ** 3 - 9800.01 * x ** 2 - 999901 * x + 10000
x0 = 0.011

if kantorovich_check(equation, x, x0):
    print("Метод сходится по теореме Канторовича")
    print("Ответ для 1 корня: ", newton_formula(equation, x, x0))
    print("Проверка для 1 корня: ", check(newton_formula(equation, x, x0)))

else:
    print("Метод не сходится")
