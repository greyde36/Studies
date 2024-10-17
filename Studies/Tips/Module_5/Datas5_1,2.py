class Human:                                       # Создание собственного класса
    def __init__(self, name, age):                 # Методы это функции внутри класса (способности)
        self.name = name
        self.age = age
        self.say_info()
        self.birthday()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age+=1
        print(f'У меня день рождения, мне теперь {self.age}')


den = Human('Денис', 22)               # Присвоение класса (при присвоении автоматически вызывается функция)
max = Human('Макс', 22)                # Атрибуты это переменные внутри класса (характеристики)

# print(den.name, den.age)
# print(max.name, max.age)
# den.say_info()
# max.say_info()