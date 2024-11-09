import os  # Данных из ОС

print('Текущая директория', os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')                   # Создать папку, если она уже существует, будет ошибка
    os.chdir('second')                   # Переименовать
print('Текущая директория', os.getcwd())
# os.makedirs(r'third\fourth')           # создание нескольких папок последовательно "\" ругается, ставим в начале r
print(os.listdir())                      # Просмотр файлов в текущей директории
os.chdir(r'C:\Users\Greyde\Desktop\Work\Urban\Studies\Tips\Module_7')  # Перейти к файлу
############################
file = [f for f in os.listdir() if os.path.isfile(f)]        # если это файл вернёт True
dirs = [d for d in os.listdir() if os.path.isdir(d)]         # если это папка вернёт True
print(dirs)
print(file)
############################
os.startfile(file[6])
print(os.stat(file[6]))                              # print(os.stat(file[6].st_size)) покажет только размер файла
os.system('pip install random2')                     # Запуск командной строки ОС и выполнение команды