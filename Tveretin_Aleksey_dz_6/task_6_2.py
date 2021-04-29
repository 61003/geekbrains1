# 2. *(вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла
# логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами, размер которых
# превышает объем ОЗУ компьютера.

list_of_tuples = []
with open('nginx_logs.txt', 'r', encoding='utf-8') as my_file:
    for line in my_file:
        string_1 = line[0:line.find(" - - ")]
        string_2 = line[line.find('] "') + 3:line.find(' /')]
        string_3 = line[line.find(' /') + 1:line.find(' HTTP')]
        my_tuple = (string_1, string_2, string_3)
        list_of_tuples.append(my_tuple)

ips = {}
for item in list_of_tuples:
    if ips.get(item[0]):
        ips[item[0]] += 1
    else:
        ips[item[0]] = 1

print(max(ips.values()))
