                #Пример 1 - raise ошибки
def greet_person(person_name):
    if person_name=='ВоланДеМорт':
        raise Exception('Мы не любим тебя, ВоланДеМорт')
    print(f'Привет, {person_name}')
#greet_person('Дорогой ученик')
#greet_person('ВоланДеМорт')
                #Пример 2 - raise ошибки, но перед этим ее обрабатываем
# try:
#     raise NameError('Привет Там')
# except NameError as exc:
#     print(f'Исключение типа {type(exc)} пролетело мимо! его параметры {exc.args}')
#     raise
                #Пример 3 - raise ошибки, в классе
# class ProZero(Exception):
#     pass
# def f(a,b):
#     if b==0:
#         raise ProZero('Деление на ноль невозможно') # Создание собственного класса ошибки
#     return a/b
# print(f(5,0))
                #Пример 4 - raise ошибки, в классе
class ProZero(Exception):
    def __init__(self,message,extra_info):
        self.message=message
        self.extra_info=extra_info
def f(a,b):
    if b==0:
        raise ProZero('Деление на ноль невозможно',{'a':a,'b':b})
    return a/b
try:
    result=f(10,0)
except ProZero as e:
    print(f'Не очень хороший день, мы словили ошибку')
    print(f'Сообщение об ошибке: {e.message}')
    print(f'Дополнительная информация: {e.extra_info}')