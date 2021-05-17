# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDivisionError(Exception):

    def __init__(self, txt):
        self.txt = txt


division = input("Введите на что делим миллион")

try:
    if division == '0':
        raise MyZeroDivisionError('не можем делить на ноль!')
    else:
        print(str(1000000 / int(division)))
except MyZeroDivisionError as err:
    print(err)
