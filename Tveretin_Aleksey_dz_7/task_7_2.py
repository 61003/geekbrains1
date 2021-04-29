# 2. *(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:

import os

with open('config.yaml', 'r', encoding='utf-8') as my_conf:
    dirs = {}
    curr_level = 0
    dir_before = None
    for line in my_conf:
        line = line.replace('\n', '')
        level = int(line.find('|--') / 3)
        is_file = True if line.find('.') > -1 else False
        dir_name = line[line.find('|--') + 3:len(line)]
        if level == 0:
            new_dir = dir_name
        elif level > curr_level:
            curr_level = level
            dir_before = new_dir
            new_dir = f'{dir_before}/{dir_name}'
        elif level == curr_level:
            new_dir = f'{dir_before}/{dir_name}'
        elif level < curr_level:
            for _ in range(curr_level - level):
                dir_before = dir_before[0:dir_before.rfind('/')]
            curr_level = level
            new_dir = f'{dir_before}/{dir_name}'
        else:
            new_dir = ''
        if not os.path.exists(new_dir):
            if is_file:
                with open(new_dir, 'w', encoding='utf-8') as my_file:
                    pass
            else:
                os.mkdir(new_dir)
