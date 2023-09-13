# Напишите функцию для транспонирования матрицы.

arr = [ [1, 2, 4, 29],
        [3, 4, 6, 1],
        [9, 7, -5, 6]]


def transpose_(array_):
    return [list(row) for row in zip(*array_)]


print(arr)
print(transpose_(arr))