# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя
# пользователя и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден,
# выбросить исключение ValueError. Пример:
#
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru

# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении;
# имеет ли смысл в данном случае использовать функцию re.compile()?

import re


def email_parse(email):
    RE_NAME = re.compile(r'(\w+)(@)(.+\.\w+)')
    try:
        if RE_NAME.match(email) != None:
            mail_group = RE_NAME.findall(email)
            mail_dict = {}
            mail_dict['username'] = mail_group[0][0]
            mail_dict['domain'] = mail_group[0][2]
            return mail_dict
        else:
            raise Exception(f'wrong email: {email}')
    except Exception as e:
        raise


print(email_parse('g100m8888@gmail.com'))
