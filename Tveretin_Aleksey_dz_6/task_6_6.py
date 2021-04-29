# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
# командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки
# значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
# a) просто запуск скрипта — выводить все записи;
# b) запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# c) запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный
# второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
#
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

def write_data(sum_of_sale):
    with open('bakery.csv', 'a', encoding='utf-8') as write_file:
        write_file.write(f'{sum_of_sale}\n')


def read_data(start_range=0, stop_range=0):
    start_range = float(start_range)
    stop_range = float(stop_range)
    with open('bakery.csv', 'r', encoding='utf-8') as read_file:
        for num, line in enumerate(read_file):
            line = line.replace('\n', '')
            if start_range > 0:
                if stop_range > 0:
                    if num + 1 >= start_range and num + 1 <= stop_range:
                        print(line)
                else:
                    if num + 1 >= start_range:
                        print(line)
            else:
                print(line)
