# 2. Дан список:
# ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
# Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных
# разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []
message = ''
for item in my_list:
    clear_item = ''
    digit_item = ''
    if item[0:1] == '+':
        clear_item = item[1:]
        digit_item = item[0:1]
    else:
        clear_item = item
    item_message = ''
    if clear_item.isdigit() and item.find('.') == -1:
        str_digit = f'{digit_item}{int(clear_item):02}'
        new_list.append('"')
        new_list.append(str_digit)
        new_list.append('"')
        item_message = f'"{str_digit}" '
    else:
        new_list.append(item)
        item_message = f"{item} "
    message += item_message

message = message[0:len(message) - 1]
print(message)
