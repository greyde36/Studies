def f1(number):
    return 10 / number
def f2():
    print('Какой хороший день')
    result_f1 = f1(0)
    return result_f1
try:
    total = f2()
    print(total)
except ZeroDivisionError as exc_1:
    print(f'Вот что пошло не так -  {exc_1}')
print('#########################################')
def f3(number):
    return 10 / number
def f4():
    print('Какой хороший день')
    summ = 0
    for i in range(-2, 2):
        summ += f3(i)
    return summ
try:
    total = f4()
    print(total)
except ZeroDivisionError as exc_2:
    print(f'Вот что пошло не так -  {exc_2}')
print('#########################################')
def f5(number):
    return total_5/number
def f6():
    try:
        result_f5=f5(0)
        print(result_f5)
    except ZeroDivisionError as exc_3:
        print(f'Внутри f5 что-то пошло не так: {exc_3}')
    return result_f5/0
try:
    f6()
except NameError as exc:
    print(f'Вот что пошло не так -  {exc}')