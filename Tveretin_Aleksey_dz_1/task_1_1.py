duration = int(input(' Введите продолжительность: '))
seconds = duration % 60

if duration < 60:
    print('{} сек'.format(seconds))
elif duration < 60 * 60:
    minutes = duration // 60
    print('{} мин {} сек'.format(minutes, seconds))
elif duration < 60 * 60 * 24:
    hours = duration // (60 * 60)
    minutes = (duration // 60) - (hours * 60)
    print('{} час {} мин {} сек'.format(hours, minutes, seconds))
else:
    days = duration // (60 * 60 * 24)
    hours = (duration // (60 * 60)) - (days * 24)
    minutes = (duration // 60) - (hours * 60) - (days * 24 * 60)
    print('{} дн {} час {} мин {} сек'.format(days, hours, minutes, seconds))
