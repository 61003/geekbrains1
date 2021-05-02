# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
#
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача,
# которая решена, например, во фреймворке django.

import os
from os.path import relpath
from shutil import copy2

root_dir = 'my_project'
new_root = 'templates'
for root, dirs, files in os.walk(root_dir):
    new_temp = f'{root_dir}/{new_root}'
    if not os.path.exists(new_temp):
        os.mkdir(new_temp)
    for dir in dirs:
        if f'{root}/{dir}'.find(f'{root_dir}/{new_root}') == -1:
            new_dir = f'{root}/{dir}'.replace(root_dir, f'{root_dir}/{new_root}')
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
    for file in files:
        if f'{root}/{dir}'.find(f'{root_dir}/{new_root}') == -1:
            ext = file.rsplit('.', maxsplit=1)[-1].lower()
            rel_path = relpath(os.path.join(root, file), root_dir)
            copy2(f'{root_dir}/{rel_path}', f'{root_dir}/{new_root}/{rel_path}')
