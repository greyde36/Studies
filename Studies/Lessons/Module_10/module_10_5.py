import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print(f'{round((time.time() - start_time),3)} секунд (линейный)')

    # Многопроцессный
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    print(f'{round((time.time() - start_time),3)} секунд (многопроцессный)')