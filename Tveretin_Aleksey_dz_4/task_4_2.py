# 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
# использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
# браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
# величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента
# передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
# регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.

from requests import get, utils


def currency_rates(val_str):
    val_str = val_str.upper()
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    if content.find(val_str) > -1:
        content = content[content.find(val_str):]
        course_beg = content.find('<Value>') + 7
        course_end = content.find('</Value>')
        course = float(content[course_beg:course_end].replace(',', '.'))
    else:
        course = None
    return course


print(currency_rates('USd'))
print(currency_rates('eur'))
