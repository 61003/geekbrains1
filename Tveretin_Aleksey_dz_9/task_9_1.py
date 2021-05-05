# 1. Создать класс TrafficLight (светофор).
#
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды,
# третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее
# сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __color = ''

    def running(self):
        if self.__color == '' or self.__color == 'green':
            self.__color = 'red'
            print(self.__color)
            sleep(7)
        elif self.__color == 'red':
            self.__color = 'yellow'
            print(self.__color)
            sleep(2)
        elif self.__color == 'yellow':
            self.__color = 'green'
            print(self.__color)
            sleep(5)


my_traffic_light = TrafficLight()
my_traffic_light.running()
my_traffic_light.running()
my_traffic_light.running()
my_traffic_light.running()
my_traffic_light.running()
