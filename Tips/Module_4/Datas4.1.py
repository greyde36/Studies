    # Из "Имя модуля" импортировать "имя переменной" как "новое название"
#from Datas4.1() import say_hi as sh             # т.к у меня стоит точка в названии применяем другой импорт
    # Импорт с нестандартным названием
import importlib
datas_module=importlib.import_module("Datas4.1()")
    # Теперь можно обращаться к функциям модуля
datas_module.say_hi()

print('Привет я из модуля 1')

sh()