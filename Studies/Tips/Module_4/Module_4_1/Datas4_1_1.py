def say_hi():
    print('Привет я из функции во втором модуле')


def main():
    a = 5
    b = 10
    print('Привет')


if __name__ == '__main__':
    main()

from random import randint # импорт рандомного числа в указанном диапазоне
print(randint(1,10))