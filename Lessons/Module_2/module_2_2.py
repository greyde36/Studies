first = int(input('Введите 1 число: '))
second = int(input('Введите 2 число: '))
third = int(input('Введите 3 число: '))
if first == second == third:
    print('3 числа равны')
elif first == second or first == third or second == third:
    print('2 числа равны')
else:
    print('0 чисел равно')