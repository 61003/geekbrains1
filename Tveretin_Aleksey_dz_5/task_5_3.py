# Есть два списка:
tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов,
# чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения. Подумать, в каких ситуациях
# генератор даст эффект.

def pairs_gen(tutors, klasses):
    my_gen = ((tutors[tutors_ind], klasses[tutors_ind]) for tutors_ind in range(0, len(tutors)))
    return my_gen


klasses_null = klasses[:]
nulls = len(tutors) - len(klasses)
for null in range(nulls):
    klasses_null.append(None)

pair = pairs_gen(tutors, klasses_null)
print(type(pair))
try:
    while True:
        print(next(pair))
except StopIteration:
    None
