name = input('Введите имя: ')                                 # Переменная которую вводит пользователь (все данные являются строкой)
print('Привет,',name)                                         # STR
age_birth = int(input('Введите ваш год рождения: '))
age = (int(2024)-age_birth)
print('В 2024 году вам было',age,'лет')

print('строка в нижнем регистре'.upper())
print('СТРОКА В ВЕРХНЕМ РЕГИСТРЕ'.lower())
print('строка в верхнем регистре'.replace('строка в верхнем','12345 в'))