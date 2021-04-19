# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
# «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные
# по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
# >>> >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": "Петр Алексеев"
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }
# Как поступить, если потребуется сортировка по ключам?

def thesaurus_adv(*args):
    names = {}
    for arg in args:
        name = arg.split()
        s_name_dict = {}
        if not names.get(name[1][0:1]):
            s_name_dict = {name[1][0:1]: ""}
            names.update(s_name_dict)
    for item in names:
        inner_names = {}
        for arg in args:
            fullname = arg.split()
            if item == fullname[1][0:1]:
                name_dict = {}
                if not inner_names.get(arg[0:1]):
                    name_dict = {arg[0:1]: [arg]}
                    inner_names.update(name_dict)
                else:
                    name = inner_names.get(arg[0:1])
                    name.append(arg)
                    name_dict = {arg[0:1]: name}
                inner_names.update(name_dict)
        update_item = {item: inner_names}
        names.update(update_item)
    return names


my_thesaurus = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
print(my_thesaurus)
