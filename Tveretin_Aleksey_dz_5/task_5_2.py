#*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.

def odd_nums(max_num):
    odd_gen = (num for num in range(1, max_num + 1, 2))
    return odd_gen

odd_to_15 = odd_nums(15)
try:
    while True:
        print(next(odd_to_15))
except StopIteration:
    None
