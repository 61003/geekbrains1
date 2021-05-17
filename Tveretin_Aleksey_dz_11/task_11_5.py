# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад
# и передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).


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

    def __init__(self, model, print_speed):
        OfficeEquipment.__init__(self, model)
        self.print_speed = print_speed


class Scaner(OfficeEquipment):

    def __init__(self, model, size):
        OfficeEquipment.__init__(self, model)
        self.size = size


class Copier(OfficeEquipment):

    def __init__(self, model, is_color):
        OfficeEquipment.__init__(self, model)
        self.is_color = is_color


canon = Printer('Canon 543', 300)
xerox = Copier('Xerox 4-555', False)
new_store = Store()
new_store.store_input(canon, 5)
print(new_store)
new_store.store_input(xerox, 4)
print(new_store)
new_store.store_input(xerox, 3)
print(new_store)
new_store.store_output(xerox, 1, 'Отдел обеспечения')
print(new_store)
new_store.store_output(xerox, 2, 'Отдел транспорта')
print(new_store)
new_store.store_output(xerox, 10, 'Отдел транспорта')
print(new_store)
new_store.show_journal()
