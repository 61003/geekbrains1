def declension(number):
    result = ''
    if number == 1:
        result = 'процент'
    elif number >= 2 and number <= 4:
        result = 'процента'
    elif number > 4:
        result = 'процентов'
    return result


for number in range(1, 21):
    print('{} {}'.format(number, declension(number)))
