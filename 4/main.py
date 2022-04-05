from sympy import diff, symbols
from sympy.abc import x, y

# X   | 2,0   | 2,3   | 2,5   | 3,0   | 3,5   | 3,8   | 4,0   |
# f(x)| 5,848 | 6,127 | 6,300 | 6,694 | 7,047 | 7,243 | 7,368 |
# x_ = 3.75

arr_x = [2.0, 2.3, 2.5, 3.0, 3.5, 3.8, 4.0]
arr_f_x = [5.848, 6.127, 6.300, 6.694, 7.047, 7.243, 7.368]
x_ = 3.75


def main_formula(arr_x_, arr_f_x_, x__):
    w_x = (x - arr_x_[len(arr_x_)])
    for i in reversed(arr_x_):
        w_x *= (x - arr_x_[i+1])
        print(w_x)
    return True


main_formula(arr_x, arr_f_x, x_)
