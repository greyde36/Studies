class Human:
    head = True
    _legs = True                                # _ защита от переопределения в дочерних классах
    __arms = True                               # __ автоматически подставляет класс

    def say_hello(self):
        print('Здравствуйте')

class Student(Human):  # Дочерний
    def about(self):
        print('Я студент')


class Teacher(Human):
    pass