class User:
    __instance__=None
    def __new__(cls, *args, **kwargs):
        print('Я в нью')
        # if cls.__instance__ is None:              # Если сделать так то ведет к одному месту в памяти
        #     cls.__instance__=super().__new__(cls)
        return super().__new__(cls)                 # Без этого new будет = None

    def __init__(self, *args, **kwargs):
        print('Я в ините')
        self.args=args
        self.kwargs=kwargs
        self.name=kwargs.get('name')
        self.age=kwargs.get('age')
        for key, value in kwargs.items():           # Универсальность для добавления новых *, **
            setattr(self,key,value)

other=[1,2,3]
user={'name': 'Den', 'age':25, 'gender':'male'}


user1 = User()
user2 = User()
print(user1 is user2)                              # Метод new создаёт новый класс который ведет к разным местам памяти
print(user1.args)
print(user1.kwargs)
user1 = User(other,user)
print(user1.args)
print(user1.kwargs)
user1 = User(*other,**user)
print(user1.name)
print(user1.age)
print(user1.gender)