def print_params(*params):                          # *args - неизвестно сколько будет параметров
    print(params)                                   # Запакованный вариант
print_params(1,2,3,4,5,6,7)                 # Всегда КОРТЕЖ

def print_params2(*params):                         # *args, **kwargs
    print(*params)                                  # Распакованный вариант
print_params2(1,2,3,4,5,6,7)

def print_params3(a,b,c):                           # **kwargs
    print(a,b,c)
list=[1,2,3]
print_params3(*list)                                # без "*" ошибка, сколько параметров столько и значений должно быть

def print_params4(a,b,c):
    print(a,b,c)
list=[1,2]
print_params4(0, *list)                          # добавление параметра, остальные добавляются сами от списка

def print_params5(a,b,c):                           # **kwargs
    print(a,b,c)
dict={'a':3,'b':2,'c':1}                            # Ключи должны соответствовать параметрам
print_params5(**dict)                               # вывод словаря

def print_params6(**kwargs):                        # **kwargs
    print(kwargs)
dict={'a':3,'b':2,'c':1}
print_params6(**dict)                               # Вывод словаря целиком (ключа и значения)

def print_params7(**kwargs):                        # **kwargs
    for key in kwargs:
        print(key)
dict={'a':3,'b':2,'c':1}
print_params7(**dict)                               # Вывод только ключей

def print_params8(**kwargs):                        # **kwargs
    for key, value in kwargs.items():
        print(key, value)
dict={'a':3,'b':2,'c':1}
print_params8(**dict)                               # Вывод ключей и параметров

def print_params9(a,b,c):                           # Совмещение словаря и списка
        print(a,b,c)
list_=[3,4]
dict={'c':5}
print_params9(*list_,**dict)