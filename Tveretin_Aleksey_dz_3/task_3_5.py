# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых
# из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках (когда каждое
# слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

import random


def get_jokes(jokes_count, is_repeat=False):
    '''Генерирует разное количество шуток из трех случайных слов с опцией искючения повторов'''
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    groups_words = []
    groups_words.append(nouns)
    groups_words.append(adverbs)
    groups_words.append(adjectives)
    jokes = []
    for _ in range(jokes_count):
        joke = ""
        for words in groups_words:
            find_joke = False
            while not find_joke:
                rand = random.randint(1, len(words))
                word = words[rand - 1]
                if is_repeat and len(jokes) > 0:
                    find_joke_in_words = False
                    for last_word in jokes:
                        if last_word.find(word) > -1:
                            find_joke_in_words = True
                            break
                    if not find_joke_in_words:
                        joke += word + ' '
                        find_joke = True
                else:
                    joke += word + ' '
                    find_joke = True
        jokes.append(joke.rstrip())
    return jokes


print(get_jokes(3, is_repeat=True))
