# 4. Реализуйте базовый класс Car.
#
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы:
# go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, name, color, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police

    def go(self, speed=30):
        self.speed = speed
        print('go')

    def stop(self):
        self.speed = 0
        print('stop')

    def turn(self, direction):
        print(f'turn {direction}')

    def show_speed(self):
        print(f'speed = {self.speed}')


class TownCar(Car):

    def show_speed(self):
        print(f'speed = {self.speed}')
        if self.speed > 60:
            print('overspeed')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'speed = {self.speed}')
        if self.speed > 40:
            print('overspeed')


class PoliceCar(Car):
    pass


ferrari = SportCar("Ferrari", "red")
print(ferrari.color, ferrari.name)
ferrari.go(200)
ferrari.show_speed()
ferrari.turn('left')
ferrari.stop()
ferrari.show_speed()

ford = TownCar("Ford", "blue")
print(ford.color, ford.name)
ford.go(80)
ford.show_speed()

bob = WorkCar("BobCat", "yellow")
print(bob.color, bob.name)
bob.go(55)
bob.show_speed()

police = PoliceCar("Police", "white", True)
print(police.color, police.name)
police.go()
police.turn("right")
police.show_speed()
