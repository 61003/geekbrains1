# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
# получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.

list_of_tuples = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        string_1 = line[0:line.find(" - - ")]
        string_2 = line[line.find('] "') + 3:line.find(' /')]
        string_3 = line[line.find(' /') + 1:line.find(' HTTP')]
        my_tuple = (string_1, string_2, string_3)
        list_of_tuples.append(my_tuple)
print(list_of_tuples)
