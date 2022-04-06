from sympy import diff, symbols
from sympy.abc import x, y

# X   | 2,0   | 2,3   | 2,5   | 3,0   | 3,5   | 3,8   | 4,0   |
# f(x)| 5,848 | 6,127 | 6,300 | 6,694 | 7,047 | 7,243 | 7,368 |
# x_ = 3.75

arr_x = [2.0, 2.3, 2.5, 3.0, 3.5, 3.8, 4.0]
arr_f_x = [5.848, 6.127, 6.300, 6.694, 7.047, 7.243, 7.368]
x_ = 3.75


def main_formula(arr_x_, arr_f_x_, x__):
    w_x = (x - arr_x_[0])

    n = 0  # указатель на текущий arr_x
    w_x_k = (x - arr_x_[n])

    for i in range(len(arr_x_) - 1):
        if arr_x_[i] - arr_x_[n] == 0:
            pass
        else:
            print(arr_x_[i])
            print(arr_x_[i + 1])
            print(arr_x_[n])

            w_x_k *= (arr_x_[n] - arr_x_[i])
    w_x_k *= (arr_x_[n] - arr_x_[len(arr_x_)-1])
    print(w_x_k)

    for i in range(len(arr_x_) - 1):
        w_x *= (x - arr_x_[i + 1])
        print(w_x)

    return w_x


print(main_formula(arr_x, arr_f_x, x_))
