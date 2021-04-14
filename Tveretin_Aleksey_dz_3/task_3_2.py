# 2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
# числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

def num_translate_adv(number):
    dict_10 = {"one": "один",
               "two": "два",
               "three": "три",
               "four": "четыре",
               "five": "пять",
               "six": "шесть",
               "seven": "семь",
               "eight": "восемь",
               "nine": "девять",
               "ten": "десять"}
    if number.lower() in dict_10:
        if number[0:1].isupper():
            result = dict_10.get(number.lower())
            result = result[0:1].upper() + result[1:]
        else:
            result = dict_10.get(number)
    else:
        result = None
    return result


print(num_translate_adv("Nine"))
