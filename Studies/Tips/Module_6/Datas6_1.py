                # Наследование
class Human:            # Базовый (родительский)
    head=True

#    def __init__(self): # Обращение к дочернему классу
#        self.about()

    def say_hello(self):    # Для избежания повторов обращений
        print('Приветствую')


class Student(Human):   # Дочерний
    head = False
    def about(self):
        print('Я студент')


class Teacher(Human):
    pass


# human=Human()         # С этим ошибка
student=Student()
print(student.head)     # Без наследия ошибка
# human.about           # Ошибка
teacher=Teacher()
student.say_hello()
teacher.say_hello()