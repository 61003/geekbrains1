# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class MyDate():
    class_str = ''

    def __init__(self, str_date):
        MyDate.class_str = str_date

    @classmethod
    def str_date_to_int(cls):
        my_year = int(cls.class_str[6:10])
        my_month = int(cls.class_str[3:5])
        my_day = int(cls.class_str[0:2])
        return my_day, my_month, my_year

    @staticmethod
    def str_validate(my_date):
        result = True
        if my_date[1] < 1 or my_date[1] > 12:
            result = False

        if my_date[2] < 1:
            result = False

        if my_date[0] < 1:
            result = False
        if (my_date[1] == 1 or my_date[1] == 3 or my_date[1] == 5 or my_date[1] == 7 or my_date[1] == 8 \
            or my_date[1] == 10 or my_date[1] == 12) and my_date[0] > 31:
            result = False
        if (my_date[1] == 4 or my_date[1] == 6 or my_date[1] == 9 or my_date[1] == 11) and my_date[0] > 30:
            result = False
        if my_date[1] == 2 and my_date[2] % 4 == 0 and my_date[0] > 29:
            result = False
        if my_date[1] == 2 and my_date[2] % 4 != 0 and my_date[0] > 28:
            result = False
        return result


my_date = MyDate('29-02-2021')
print(my_date.str_date_to_int())
print(my_date.str_validate(my_date.str_date_to_int()))
