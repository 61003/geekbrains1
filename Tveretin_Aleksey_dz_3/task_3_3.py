# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?

def thesaurus(*args):
    names = {}
    for arg in args:
        name_dict = {}
        if not names.get(arg[0:1]):
            name_dict = {arg[0:1]: [arg]}
            names.update(name_dict)
        else:
            name = names.get(arg[0:1])
            name.append(arg)
            name_dict = {arg[0:1]: name}
        names.update(name_dict)
    return names


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Ирина", "Марфа"))
