class Human:
    def __init__(self, name, group):
        self.name = name
        super().__init__(group)
        super().about()

    def info(self):
        print(f'Привет меня зовут {self.name}')


class StudentGroup:                                      # Миксед
    def __init__(self, group):
        self.group = group

    def about(self):
        print(f'{self.name} учится в группе {self.group}')

class Student(Human, StudentGroup):
    def __init__(self, name, place, group):
        super().__init__(name, group)                    # Передача в родительский класс
        self.place = place
        super().info()


#print('Сергей')
#print(human.name)
student = Student('Макс', 'Урбан', 'Python')
print(Student.mro())                                     # список последовательности классов