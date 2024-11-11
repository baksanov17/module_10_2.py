import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        warrior = 100
        for day in range(1, 101):
            if warrior > 0:
                warrior = warrior - self.power
                time.sleep(1)
                print(f'{self.name} сражается {day} дней, осталось {warrior} воинов')
            else:
                print(f'{self.name} одержал победу спустя {day} дней(дня)')
                break




# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончились!')