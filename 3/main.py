from sympy import cos, diff, symbols
from sympy.abc import x, y

# Вариант 2
# cos(x-1) + y = 0.5
# x - cos(y) = 3

# Используя метод простой итерации решить систему
# уравнений с точностью до 0.001. Корни отделить графически.

reduced_y = cos(x - 1) + y - 0.5
reduced_x = x - cos(y) - 3

x0 = 3.33
y0 = 1.19


def convergence_condition(x_0, y_0, func_y, func_x):  # Проверка сходимости
    x, y = symbols('x y')
    partial_derivative_red_y_x = diff(func_y, x).subs(x, x_0)
    partial_derivative_red_y_y = diff(func_y, y).subs(y, y_0)

    partial_derivative_red_x_x = diff(func_x, x).subs(x, x_0)
    partial_derivative_red_x_y = diff(func_x, y).subs(y, y_0)

    if max(partial_derivative_red_y_x, partial_derivative_red_y_y, partial_derivative_red_x_x,
           partial_derivative_red_x_y) <= 1:
        print("Метод сходится")
        # print(partial_derivative_red_y_x, "\n", partial_derivative_red_y_y, "\n", partial_derivative_red_x_x, "\n",
        #       partial_derivative_red_x_y)
    else:
        print("Метод не сходится")
        # print(partial_derivative_red_y_x, "\n", partial_derivative_red_y_y, "\n", partial_derivative_red_x_x, "\n",
        #       partial_derivative_red_x_y)


def iterative_method(x_0, y_0, func_y, func_x):
    exp = 0.001
    x_n = x_0
    y_n = y_0
    max_iteration = 100
    k = 0
    while k <= max_iteration:
        k += 1
        x_n1 = func_x.subs([(x, x_n), (y, y_n)])
        y_n1 = func_y.subs([(x, x_n), (y, y_n)])

        print("x_n1", x_n1)
        print("x_n", x_n)

        print("y_n1", y_n1)
        print("y_n", y_n)

        if abs(x_n1 - x_n) <= exp and abs(y_n1 - y_n) <= exp:
            break
        x_n = x_n1
        y_n = y_n1

    return x_n, y_n


def check(func_y, func_x, iterative_method_result):
    x_n = iterative_method_result[0]
    y_n = iterative_method_result[1]
    check_1 = func_y.subs([(x, x_n), (y, y_n)])
    check_2 = func_x.subs([(x, x_n), (y, y_n)])
    print('cos(x - 1) + y - 0.5 =', check_1)
    print('x - cos(y) - 3 = ', check_2)


convergence_condition(x0, y0, reduced_y, reduced_x)
print(iterative_method(x0, y0, reduced_y, reduced_x))
check(reduced_y, reduced_x, iterative_method(x0, y0, reduced_y, reduced_x))
