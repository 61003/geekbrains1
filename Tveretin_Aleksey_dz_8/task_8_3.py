# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
#
# def type_logger...
#     ...
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
#
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)

def type_logger(func):
    def wrapper(*args):
        results = []
        result_of_func = func(*args)
        for arg in args:
            types = []
            types.append(arg)
            types.append(type(arg))
            results.append(types)
        result = func.__name__ + '('
        for my_arg in results:
            result += f'{my_arg[0]}: {my_arg[1]}, '
        result = result[:-2] + ')'
        print(result)
        print(type(result))
        return result_of_func

    return wrapper


@type_logger
def calc_cube(x, y):
    result = x ** y
    return result


a = calc_cube(8, 6)
print(a)
