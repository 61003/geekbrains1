# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
#
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
import os

with open('task_7_1.config', 'r', encoding='utf-8') as my_conf:
    dirs = {}
    curr_level = 0
    dir_before = None
    for line in my_conf:
        line = line.replace('\n', '')
        level = int(line.find('|') / 4)
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
            curr_level = level
            dir_before = dir_before[0:dir_before.rfind('/')]
            new_dir = f'{dir_before}/{dir_name}'
        else:
            new_dir = ''
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)

