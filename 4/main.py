# X   | 2,0   | 2,3   | 2,5   | 3,0   | 3,5   | 3,8   | 4,0   |
# f(x)| 5,848 | 6,127 | 6,300 | 6,694 | 7,047 | 7,243 | 7,368 |
# x_ = 3.75


def main_formula(points, x_value):
    value = 0
    for DOTS in points:
        omega = 1
        for point_u in points:
            if point_u != DOTS:
                omega = omega * (x_value - point_u[0])
        d_omega = 1
        for point_d in points:
            if point_d != DOTS:
                d_omega = d_omega * (DOTS[0] - point_d[0])
        value = value + (DOTS[1] * omega) / d_omega
    return value


dots = [[2, 5.848], [2.3, 6.127], [2.5, 6.300], [3.0, 6.694], [3.5, 7.047], [3.8, 7.243], [4.0, 7.368]]
x_ = 3.5

print('Полученное значение = ', main_formula(dots, x_), f'в X = {x_}')

