def summa(n):
    if n == 0:
        return 0
    else:
        return n + summa(n - 1)                                 # Рекурсия


print(summa(5))



stack = []
stack.append(1)
print('Добавили элемент' , stack)
stack.append(2)
print('Добавили элемент' , stack)
stack.append(3)
print('Добавили элемент' , stack)
print(stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)
stack.pop()
print('Убрали элемент', stack)