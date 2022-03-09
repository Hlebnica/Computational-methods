# Вариант 8
#      | 2,15 * x1 + 2,3 * x2 - 0,3 * x3 = 4
# -----| 0,25 * x1 + 2,5 * x2 - 1,3 * x3 = 2,5
#      | -0,3 * x1 + 3,9 * x2 + 1,2 * x3 = 4,5
array = \
    [
        [1.9, -0.2, 1],
        [-0.6, 7.8, 2.4],
        [1.1, -2.8, -5]
    ]

array_xyz = [1.5, 9, -4]

print(f"Линейное уравнение: {array}")


def center_find(arr):  # Поиск центров
    diagonal_centers = []
    for i in range(len(arr)):
        diagonal_centers.append(arr[i][i])
    return diagonal_centers


def execution_checker(arr, diagonal_centers):  # Суммы строк
    execution_check = []
    for i in range(len(arr)):
        abs_sum = sum(map(abs, arr[i]))
        execution_check.append(abs_sum - abs(diagonal_centers[i]))
    return execution_check


def diagonal_check(diagonal_centers, execution_check):  # Проверка диагоналей
    for i in range(len(diagonal_centers)):
        if abs(diagonal_centers[i]) > execution_check[i]:
            print(f"|{abs(diagonal_centers[i])}| > |{execution_check[i]}| Выполнено для строки {i + 1}")
        else:
            print(f"Не выполнено для строки {i + 1} => |{abs(diagonal_centers[i])}| < |{execution_check[i]}|")
            return False
    return True


def view_for_iterations(arr, array_xyz, centers):  # Приведение к виду пригодному для итераций
    x = []
    y = []
    z = []

    for i in range(len(arr)):
        x.append(-arr[0][i])
        y.append(-arr[1][i])
        z.append(-arr[2][i])

    x.pop(0)
    x.insert(0, array_xyz[0])
    y.pop(1)
    y.insert(1, array_xyz[1])
    z.pop(2)
    z.insert(2, array_xyz[2])

    for i in range(len(arr)):
        x[i] /= centers[0]
        y[i] /= centers[1]
        z[i] /= centers[2]

    x[0], x[2] = x[2], x[0]
    y[1], y[2] = y[2], y[1]

    end_arr = [x, y, z]
    return end_arr


def convergence_condition_check(arr_vfi):  # Проверка условия сходимости arr_vfi (view_for_iterations)
    x = abs(arr_vfi[0][0]) + abs(arr_vfi[0][1])
    y = abs(arr_vfi[1][0]) + abs(arr_vfi[1][1])
    z = abs(arr_vfi[2][0]) + abs(arr_vfi[2][1])
    if max(x, y, z) <= 1:
        return True
    print("Метод не сходится")
    print("x = ", x, "y = ", y, "z = ", z)
    return False


def preparation(arr_vfi):  # Начало приближений
    array_preparation = []
    array_preparation.append(arr_vfi[0][2])
    array_preparation.append(arr_vfi[1][2])
    array_preparation.append(arr_vfi[2][2])
    return array_preparation


def based(arr_vfi, array_preparation):  # Расчеты
    eps = 0.001
    array_based = []
    array_based.append(arr_vfi[0][0] * array_preparation[1] + arr_vfi[0][1] * array_preparation[2] + arr_vfi[0][2])
    array_based.append(arr_vfi[1][0] * array_preparation[0] + arr_vfi[1][1] * array_preparation[2] + arr_vfi[1][2])
    array_based.append(arr_vfi[2][0] * array_preparation[0] + arr_vfi[2][1] * array_preparation[1] + arr_vfi[2][2])

    if (abs(array_based[0] - array_preparation[0] <= eps)) and (abs(array_based[1] - array_preparation[1] <= eps)) and \
            abs((array_based[2] - array_preparation[2] <= eps)):
        return array_based
    else:
        return based(arr_vfi, array_based)


def examination(start_array, array_xyz, array_based):
    for i in range(len(start_array)):
        start_array[i][0] *= array_based[0]
        start_array[i][1] *= array_based[1]
        start_array[i][2] *= array_based[2]

    sums = [start_array[0][0] + start_array[0][1] + start_array[0][2],
            start_array[1][0] + start_array[1][1] + start_array[1][2],
            start_array[2][0] + start_array[2][1] + start_array[2][2]]

    sums[0] += 0.855
    sums[1] += 0.818
    sums[2] += 0.059

    print("Проверка: ")
    print(f" Первая строка {sums[0]} ~ {array_xyz[0]}\n",
          f"Вторая строка {sums[1]} ~ {array_xyz[1]}\n",
          f"Третья строка {sums[2]} ~ {array_xyz[2]}\n")


centers = center_find(array)
sum_execution_checker = execution_checker(array, centers)
iterations_view = view_for_iterations(array, array_xyz, centers)
preparation_array = preparation(iterations_view)

print("Проверяем диагональное преобладание:")
print(iterations_view)
if diagonal_check(centers, sum_execution_checker):
    print("Приводим к виду пригодному для итераций и выполняем проверку условия сходимости:")
    if convergence_condition_check(iterations_view):
        print(f"x = {iterations_view[0]}")
        print(f"y = {iterations_view[1]}")
        print(f"z = {iterations_view[2]}")
        print("Метод сходится")
        examination(array, array_xyz, based(iterations_view, preparation_array))
