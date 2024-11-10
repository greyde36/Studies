try:
    ... #пишем здесь код с возможной ошибкой
except:
    ... #пишем здесь блок кода в случае возникновения ошибки
finally:
    ... #выполняется всегда вне зависимости от else или except
################################################
try:
    truba= a+b
    truba= 10/0
except ZeroDivisionError:                   # Указывается класс ошибки (необязательно, может быть несколько)
    print('Нельзя делить на ноль!')
except NameError:
    print("Ошибка переменных")
################################################
try:
    truba= 10/0
except ZeroDivisionError as exc:
    print(f'вот что пошло не так {exc}')
################################################
try:
    file=open('blabla.txt')
except OSError as exc:
    print(f'вот что пошло не так {exc} параметры {exc.args}')
################################################
g=int(input('Введите число: '))
try:
    result=10*(1/g)
except ZeroDivisionError as exc:
    print('нельзя делить на ноль!',exc)
else:
    print('ура, мы не делим на ноль')
finally:
    print('файнали, мы закончили')