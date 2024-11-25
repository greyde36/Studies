import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100
        self.day_fight = 1

    def run(self):
        print(f'{self.name}, на нас напали! ')
        while self.enemy > 0:
            self.enemy -= self.power
            time.sleep(1)
            print(f'{self.name} сражается {self.day_fight} день, осталось {self.enemy} воинов ')
            if self.enemy <= 0:
                print(f'{self.name} одержал победу спустя {self.day_fight} дней(дня)! ')
            self.day_fight += 1


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()