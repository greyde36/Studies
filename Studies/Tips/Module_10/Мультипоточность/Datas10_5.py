# Класс Event
from threading import Thread,Event
import time

def first_worker():
    print('Первый рабочий приступил к своей задаче')
    event.wait()
    print('Первый рабочий продолжил выполнять задачу')
    time.sleep(3)
    print('Первый рабочий закончил выполнять задачу')

def second_worker():
    print('Второй рабочий приступил к своей задаче')
    time.sleep(5)
    print('Второй рабочий закончил выполнять задачу')
    event.set()

event=Event()
event.set()
event.clear()
print(event.is_set())
thread1=Thread(target=first_worker)
thread2=Thread(target=second_worker)
thread1.start()
thread2.start()
# print(event.set())
# event.wait(timeout=3)
# print(event.is_set())