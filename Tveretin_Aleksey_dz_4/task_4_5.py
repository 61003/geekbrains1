# 5. *(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли. Например:
# python task_4_5.py USD
# 75.18, 2020-09-05

from utils import currency_rates
from sys import argv

for arg in argv[1:]:
    print(currency_rates(arg))
