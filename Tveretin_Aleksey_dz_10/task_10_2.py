# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
# классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, size, name):
        self.size = size
        self.name = name

    @abstractmethod
    def cloth_amount(self):
        pass


class Suit(Clothes):

    @property
    def cloth_amount(self):
        return 2 * self.size + 0.3


class Coat(Clothes):

    @property
    def cloth_amount(self):
        return self.size / 6.5 + 0.5


my_coat = Coat(6.5, 'Пальто')
print(f'Для {my_coat.name} требуется {my_coat.cloth_amount} ткани')

my_suit = Suit(2, 'Костюм')
print(f'Для {my_suit.name} требуется {my_suit.cloth_amount} ткани')
