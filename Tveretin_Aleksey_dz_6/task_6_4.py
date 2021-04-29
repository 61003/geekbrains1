# 4. *(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ
# (разумеется, не нужно реально создавать такие большие файлы, это просто задел на будущее проекта).
# Только теперь не нужно создавать словарь с данными. Вместо этого нужно сохранить объединенные данные в новый файл
# (users_hobby.txt). Хобби пишем через двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

from os import remove

write_file = open('users_hobby.txt', 'a', encoding='utf-8')

with open('users.csv', 'r', encoding='utf-8') as user_file, open('hobby.csv', 'r', encoding='utf-8') as hobby_file:
    while True:
        user = user_file.readline()
        hobby = hobby_file.readline()
        if user:
            user_str = user.replace('\n', '')
            if hobby:
                hobby_str = hobby.replace('\n', '')
            else:
                hobby_str = None
        else:
            if hobby:
                write_file.close()
                remove('users_hobby.txt')
                raise Exception("Too many hobby entries")
            else:
                break
        write_string = f'{user_str}: {hobby_str}\n'
        write_file.write(write_string)

write_file.close()
