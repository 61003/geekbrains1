# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex():

    def __init__(self, i, j):
        self.i = i
        self.j = j

    def __str__(self):
        return f'{self.i}, {self.j}j'

    def __add__(self, other):
        return Complex(self.i + other.i, self.j + other.j)

    def __mul__(self, other):
        return Complex(self.i * other.i - self.j * other.j, self.i * other.j + self.j * other.i)


my_complex_1 = Complex(1, -2)
print(my_complex_1)
my_complex_2 = Complex(3, 5)
print(my_complex_2)
my_complex_3 = my_complex_1 + my_complex_2
print('add', my_complex_3)
my_complex_4 = my_complex_1 * my_complex_2
print('mul', my_complex_4)
