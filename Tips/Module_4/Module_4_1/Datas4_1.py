#         Из "Имя модуля" импортировать "имя переменной" как "новое название"
#   from Datas4.1 import say_hi as sh             # т.к у меня стоит точка в названии применяем другой импорт
#     Импорт с нестандартным названием
# import importlib
# datas_module=importlib.import_module("Datas4.1")
#     Теперь можно обращаться к функциям модуля
# datas_module.say_hi()
# from module_4_1.Datas4_1_1 import main                    # импорт из папки внутри запущенного файла
# если при импорте из папки Package есть файл __init__ будет запускаться только он
# from .module_4_1.Datas4_1_1 import main                   # импорт из текущей папки запущенного файла
# from ..module_4_1.Datas4_1_1 import main                  # импорт из предыдущей папки запущенного файла



from Datas4_1_1 import say_hi as sh
import sys
import math # математика
import random # рандом
import tkinter # создание приложения
# если вызвать импорт внутри функции он будет существовать только внутри функции
# если в импортируемом файле будет другой импортируемый файл будет ошибка
print('Привет я из модуля 1')
for path in sys.path:
    print(path)
sh()