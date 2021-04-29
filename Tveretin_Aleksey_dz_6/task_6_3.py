# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно,
# что при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

with open('users.csv', 'r', encoding='utf-8') as user_file:
    users = user_file.read()
with open('hobby.csv', 'r', encoding='utf-8') as hobby_file:
    hobby = hobby_file.read()
users = users.split('\n')
hobby = hobby.split('\n')
if len(users) < len(hobby):
    raise Exception("Too many hobby entries")
elif len(users) > len(hobby):
    for _ in range(len(users) - len(hobby)):
        hobby.append(None)
else:
    None
hobby_users = {}
for item in range(len(users)):
    hobby_users[users[item]] = hobby[item]
with open('hobby_users.csv', 'w', encoding='utf-8') as hobby_new_file:
    hobby_new_file.write(str(hobby_users))
