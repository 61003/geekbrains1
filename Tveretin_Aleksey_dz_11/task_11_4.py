# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов.
# В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.


class Store():
    pass


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


printer = Printer('yy', 99)
