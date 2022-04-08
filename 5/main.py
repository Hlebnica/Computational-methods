from scipy import integrate
from sympy import diff, sqrt
from sympy.abc import x


#  Формула прямоугольников
#  1
#  |
#  | (x^2/2)dx
#  |
#  -1
#

def func(x):
    return (x ** 2) / 2


def printer(upper_limit_, lower_limit_, function):
    print(upper_limit_)
    print('|')
    print('|', f'{function}dx = ', integral[0])
    print('|')
    print(lower_limit_)


def m_2():
    return True


lower_limit = -1
upper_limit = 1

integral = integrate.quad(func, lower_limit, upper_limit)

printer(upper_limit, lower_limit, "(x^2/2)")
