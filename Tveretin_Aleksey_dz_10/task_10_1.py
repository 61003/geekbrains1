# . Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
# | 3 5 8 3 |
# | 8 3 7 1 |

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        result = ''
        for raw in self.matrix:
            raw_str = ''
            for col in raw:
                raw_str += str(col) + ' '
            result += raw_str + '\n'
        return result

    def __add__(self, other):
        matrix_list = []
        for raw in range(len(self.matrix)):
            raw_list = []
            for col in range(len(self.matrix[raw])):
                raw_list.append(self.matrix[raw][col] + other.matrix[raw][col])
            matrix_list.append(raw_list)
        return Matrix(matrix_list)


my_matrix_1 = Matrix([[1, 2], [4, 2], [6, 8]])
print(my_matrix_1)
print()
my_matrix_2 = Matrix([[5, 6], [3, 33], [4, 0]])
print(my_matrix_2)
print()
my_matrix_3 = my_matrix_1 + my_matrix_2
print(my_matrix_3)
