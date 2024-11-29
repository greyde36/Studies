import multiprocessing
import time
import threading

counter=0
def first_worker(n):
    global counter
    for i in range(n):
        counter+=1
        time.sleep(1)
    print('Первый рабочий изменил значение счётчика', counter)

def second_worker(n):
    global counter
    for i in range(n):
        counter+=1
        time.sleep(1)
    print('Второй рабочий изменил значение счётчика', counter)



if __name__=="__main__":
    # thread1=threading.Thread(target=first_worker,args=(10,))                  # Потоки выполняются
    # thread2=threading.Thread(target=second_worker,args=(5,))                  # последовательно
    # thread1.start()
    # thread2.start()
    process1=multiprocessing.Process(target=first_worker,args=(10,))            # Процессы выполняются
    process2=multiprocessing.Process(target=second_worker,args=(15,))           # одновременно
    process1.start()                            # Процессы работают только если есть " if __name__=="__main__": "
    process2.start()