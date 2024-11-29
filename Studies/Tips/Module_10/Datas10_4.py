from queue import Queue
import time
import threading


def getter(queue):
    while True:              # Повторять пока список не будет пуст ( while not queue.empty() )
        time.sleep(3)
        item = queue.get()
        print('Взят элемент ', item)

q=Queue(maxsize=10)                       # Ограничение на максимальное значение в очереди
thread1=threading.Thread(target=getter,args=(q,), daemon=True)
thread1.start()

for i in range(10):
    time.sleep(2)
    q.put(i)
    print(threading.current_thread(),'положил в очередь элемент', i)

# q = Queue()                             # 1 Создание очереди
# q.put(5)                                # 4 Положить элемент в очередь
# print(q.get(timeout=2))                 # 2 Достать элемент из очереди, таймаут сколько ждать получение элемента и продолжить
# print('Конец программы')                # 3 Ничего не выводит т.к нечего взять, процесс остановлен и ждёт