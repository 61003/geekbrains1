# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class WrongType(Exception):

    def __init__(self, txt):
        self.txt = txt


class Store():

    def __init__(self):
        self.store_list = {}
        self.output_journal = []

    def __str__(self):
        result = ''
        for item, val in self.store_list.items():
            result += f'{item.model} - {val} \n'
        return result

    def show_journal(self):
        for item in self.output_journal:
            print(f'{item}')

    def store_input(self, equipment, count):
        if self.store_list.get(equipment) == None:
            self.store_list[equipment] = count
        else:
            self.store_list[equipment] = self.store_list.get(equipment) + count

    def store_output(self, equipment, count, department):
        if self.store_list.get(equipment) != None:
            if count > self.store_list.get(equipment):
                print('Нельзя выдать больше чем есть на складе')
            else:
                self.store_list[equipment] = self.store_list.get(equipment) - count
                self.output_journal.append((equipment.model, department, count))
                if self.store_list[equipment] <= 0:
                    self.store_list.pop(equipment)


class OfficeEquipment():

    def __init__(self, model):
        self.model = model


class Printer(OfficeEquipment):

    def __init__(self, model, print_speed=0):
        OfficeEquipment.__init__(self, model)
        self.print_speed = print_speed


class Scaner(OfficeEquipment):

    def __init__(self, model, size=0):
        OfficeEquipment.__init__(self, model)
        self.size = size


class Copier(OfficeEquipment):

    def __init__(self, model, is_color=None):
        OfficeEquipment.__init__(self, model)
        self.is_color = is_color


new_store = Store()

while True:
    try:
        eq_type = input('введите тип товара (1 - принтер, 2 - сканер, 3 - ксерокс) или stop')
        if eq_type == 'stop':
            break
        if eq_type == '1' or eq_type == '2' or eq_type == '3':
            item_model = input("введите модель ")
            item_count = input("введите количество")
            if not item_count.isdigit():
                raise WrongType('введите число')
            else:
                if eq_type == '1':
                    item = Printer(item_model)
                elif eq_type == '2':
                    item = Scaner(item_model)
                elif eq_type == '3':
                    item = Copier(item_model)
                new_store.store_input(item, item_count)
                print(new_store)
        else:
            raise WrongType('неверный тип товара')
            continue
    except WrongType as err:
        print(err)
