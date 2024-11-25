import time
import threading
import random


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            plus_balans = random.randint(50, 500)
            self.balance += plus_balans
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {plus_balans}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            minys_balans = random.randint(50, 500)
            print(f'Запрос на {minys_balans}')
            if minys_balans <= self.balance:
                self.balance -= minys_balans
                print(f'Снятие: {minys_balans}. Баланс {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
            self.lock.acquire()


bk = Bank()
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')