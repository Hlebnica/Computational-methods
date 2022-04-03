from sympy import cos, diff
from sympy.abc import x, y

# Вариант 2
# cos(x-1) + y = 0.5
# x - cos(y) = 3

# Используя метод простой итерации решить систему
# уравнений с точностью до 0.001. Корни отделить графически.

reduced_y = 0.5 - cos(x - 1)
reduced_x = 3 + cos(y)

x0 = 3.33
y0 = 1.19

