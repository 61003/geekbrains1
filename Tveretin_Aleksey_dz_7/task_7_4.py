# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи — верхняя граница размера файла (пусть будет кратна 10),
# а значения — общее количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
# но больше предыдущей (начинаем с 0), например:
#
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
#
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.

import os

root_dir = '/users/aleksey/downloads'
sizes_list = []
for root, dirs, files in os.walk(root_dir):
    for file in files:
        file_size = os.stat(f'{root}/{file}').st_size
        sizes_list.append(file_size)
stat_dict = {}
for i in range(1, len(str(max(sizes_list))) + 1):
    listz = filter(lambda number: number <= 10 ** i and number > 10 ** (i - 1), sizes_list)
    range_list = list(listz)
    stat_dict[10 ** i] = len(range_list)

print(stat_dict)
