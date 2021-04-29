# 5. **(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя
# обоих исходных файлов и имя выходного файла. Проверить работу скрипта.


from os import remove
from sys import argv


def write_hobby_file(users_file, hobby_file, new_file):
    write_file = open(new_file, 'a', encoding='utf-8')
    with open(users_file, 'r', encoding='utf-8') as user_file, open(hobby_file, 'r', encoding='utf-8') as hobby_file:
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


write_hobby_file(argv[1], argv[2], argv[3])
