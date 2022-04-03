from sympy import cos, diff, symbols
from sympy.abc import x, y

# Вариант 2
# cos(x-1) + y = 0.5
# x - cos(y) = 3

# Используя метод простой итерации решить систему
# уравнений с точностью до 0.001. Корни отделить графически. .subs(x, x_0)

# y = cos(x-1) + 2y - 0.5
# x = 2x - cos(y) - 3

reduced_y = cos(x - 1) + y - 0.5
reduced_x = x - cos(y) - 3

x0 = 3.33
y0 = 1.19


def convergence_condition(x_0, y_0, reduce_y, reduce_x):  # Проверка сходимости
    x, y = symbols('x y')
    partial_derivative_red_y_x = diff(reduce_y, x).subs(x, x_0)
    partial_derivative_red_y_y = diff(reduce_y, y).subs(y, y_0)

    partial_derivative_red_x_x = diff(reduce_x, x).subs(x, x_0)
    partial_derivative_red_x_y = diff(reduce_x, y).subs(y, y_0)

    if max(partial_derivative_red_y_x, partial_derivative_red_y_y, partial_derivative_red_x_x,
           partial_derivative_red_x_y) <= 1:
        print("Метод сходится")
        print(partial_derivative_red_y_x, "\n", partial_derivative_red_y_y, "\n", partial_derivative_red_x_x, "\n",
              partial_derivative_red_x_y)
    else:
        print("Метод не сходится")
        print(partial_derivative_red_y_x, "\n", partial_derivative_red_y_y, "\n", partial_derivative_red_x_x, "\n",
              partial_derivative_red_x_y)


def iterative_method(x_0, y_0, reduce_y, reduce_x):
    exp = 0.0001
    x_n = x_0
    y_n = y_0
    
    pass


convergence_condition(x0, y0, reduced_y, reduced_x)
