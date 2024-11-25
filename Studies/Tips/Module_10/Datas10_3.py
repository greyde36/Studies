import threading

counter = 0
lock = threading.Lock()                     # Замок синхронизации (для последовательного выполнения)


def increment(name):
    global counter
    try:                                    # Чтобы поймать ошибку
        lock.acquire()                      # Активация замка синхронизации
        for i in range(1000):
            counter += 1
            print(name, counter)
    except Exception:
        pass
    finally:
        lock.release()                      # Разблокировка для продолжения кода
        # lock.locked()                     # Закрыт(True) или открыт(False) поток


def decrement(name):
    global counter
    with lock:                              # Сокращение кода чтобы не писать acquire и release
        for i in range(1000):               # сам открывает и закрывает, как работа с файлами
            counter -= 1
            print(name, counter)


thread1 = threading.Thread(target=increment, args=('thread1 ',))
thread2 = threading.Thread(target=decrement, args=('thread2 ',))
thread3 = threading.Thread(target=increment, args=('thread3 ',))
thread4 = threading.Thread(target=decrement, args=('thread4 ',))
thread1.start()
thread2.start()
thread3.start()
thread4.start()