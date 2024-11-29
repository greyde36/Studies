import time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f"Какое-то слово № {i+1}\n")
            time.sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")

start_time=time.time()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")            # последовательное выполнение
end_time=time.time()
print(f'Работа потоков {end_time-start_time}')
start_time=time.time()
thread1 = threading.Thread(target=write_words, args=(10, "example5.txt"))       # запуск всех одновременно
thread2 = threading.Thread(target=write_words, args=(30, "example6.txt"))
thread3 = threading.Thread(target=write_words, args=(200, "example7.txt"))
thread4 = threading.Thread(target=write_words, args=(100, "example8.txt"))
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()
end_time=time.time()
print(f'Работа потоков {end_time-start_time}')