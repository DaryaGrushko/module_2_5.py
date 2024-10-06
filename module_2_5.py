# Домашняя работа по уроку "Функции в Python.Функция с параметром"
# Задача "Матрица воплоти"
def get_matrix(n, m, value):  # n строк, m столбцов, value значения
    matrix = []
    # print ('matrix = ', matrix)
    for i in range(n):
        matrix.append([])
        # print('i =', i,'matrix', matrix )
        for j in range(m):
            matrix[i].append(value)
            # print('j = ', j, 'matrix', matrix)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print('result1 = ', result1)
print('result2 = ', result2)
print('result3 = ', result3)
