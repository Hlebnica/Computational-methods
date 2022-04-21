from scipy import integrate
from sympy import diff
from sympy.abc import x

#  Формула прямоугольников
#  1
#  |
#  | (x^2/2)dx
#  |
#  -1
#

originalFunc = (x ** 2) / 2  # функция
lower_limit = -1  # нижний предел
upper_limit = 1  # верхний предел
n = 10  # на какое кол-во частей делить отрезок
h = 0.2  # шаг деления


def func(x):
    return (x ** 2) / 2


def true_integral(upper_limit_, lower_limit_, function):  # Вывод интеграла с точным значением
    print(f'{upper_limit_}\n|\n|{function}dx = {integral[0]}\n|\n{lower_limit_}')


def rectangle_method(func_, lower_limit_, upper_limit_, h_, n_):  # Формула с методом прямоугольников
    lower_limit_now = lower_limit_ + 0.1
    sum_elements = (func_.subs(x, lower_limit_now))
    for i in range(n_ - 1):
        if lower_limit_now < upper_limit_:
            lower_limit_now += h_
            sum_elements += (func_.subs(x, lower_limit_now))

    rectangle_answer = sum_elements * h_
    return rectangle_answer


def m_2(x_, function, lower_limit_):
    m2 = abs(diff(function, x_, 2).subs(x_, lower_limit_))
    return m2


def r_less_equal_m2(m2_, h_, upper_limit_, lower_limit_):
    r = m2_ * (((h_ ** 2) * (upper_limit_ - lower_limit_)) / 24)
    return r


def comparison(true_integral_result_, rectangle_method_result_):
    result = abs(true_integral_result_ - rectangle_method_result_)
    return result


integral = integrate.quad(func, lower_limit, upper_limit)
m2_result = m_2(x, originalFunc, lower_limit)
r_less_equal_m2_result = r_less_equal_m2(m2_result, h, upper_limit, lower_limit)
rectangle_method_result = rectangle_method(originalFunc, lower_limit, upper_limit, h, n)
comparison_result = comparison(integral[0], rectangle_method_result)

true_integral(upper_limit, lower_limit, "(" + str(originalFunc).replace('**', '^') + ")")
print("Квадратурная формула прямоугольников = ", rectangle_method_result)
print(f"M2 = sup |f''(x)| = |f''({lower_limit})| = ", m2_result)
print(f"R <= M2 * ((h^2 * (b - a)) / 24) = {r_less_equal_m2_result}")
print(
    f"Сравнение точного значения интеграла и полученного |{integral[0]} - {rectangle_method_result}| "
    f"= {comparison_result}")
