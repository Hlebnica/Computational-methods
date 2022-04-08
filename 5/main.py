from scipy import integrate


#  Формула прямоугольников
#  1
#  |
#  | (x^2/2)dx
#  |
#  -1
#

def func(x):
    return (x ** 2) / 2


integral = integrate.quad(func, -1, 1)

print('', integral[0])
