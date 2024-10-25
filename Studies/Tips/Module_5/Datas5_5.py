class Human:

    Head=True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age+=1
        print(f'У меня день рождения, мне теперь {self.age}')

    def __str__(self):
        return f'{self.name}'

    def __len__(self):
        return self.age

    def __lt__(self, other):            # меньше
        return self.age < other.age

    def __gt__(self, other):            # больше
        return self.age > other.age

    def __eq__(self, other):            # равно
        return self.name == other.name and self.age == other.age

    def __bool__(self):                 # истина или нет
        return bool(self.age)           # любое число отличное от 0 будет True


den = Human('Денис', 22)
max = Human('Макс', 22)
if den:
    den.say_info()
print(den<max)
print(den>max)
print(den==max)
max.name="Денис"
print(den==max)
max.birthday()
print(den<max)
print(den>max)
print(den)
print(Human.Head)