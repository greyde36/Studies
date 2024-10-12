import tkinter as tk


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2                                                            # Функция получение веденных переменных


def insert_values(value):
    answer_entry.delete(0, 'end')                                     # Удаления старого ответа
    answer_entry.insert(0, value)                                         # Функция вывода ответа


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)                                                          # Функция сложения


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)                                                          # Функция вычитания


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)                                                          # Функция деления


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)                                                          # Функция умножения


window = tk.Tk()                                                                 #   |->  #Создание окна
window.title('Калькулятор')                                                      #   |  Название окна
window.geometry("350x350")                                                       #   |  Размер окна
window.resizable(False, False)                                      #   |  Запрет на изменения размеров окна
button_add = tk.Button(window, text="+", width=2, height=2, command=add)         #   |  Создать кнопку
button_add.place(x=100, y=200)                                                   #   |  Расположение кнопки по координатам
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)         #   |
button_sub.place(x=150, y=200)                                                   #   |
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)         #   |
button_mul.place(x=200, y=200)                                                   #   |
button_div = tk.Button(window, text="/", width=2, height=2, command=div)         #   |
button_div.place(x=250, y=200)                                                   #   |
number1_entry = tk.Entry(window, width=28)                                       #   |  Entry текстовое после для ввода данных
number1_entry.place(x=100, y=75)                                                 #   |
number2_entry = tk.Entry(window, width=28)                                       #   |
number2_entry.place(x=100, y=150)                                                #   |
answer_entry = tk.Entry(window, width=28)                                        #   |  Текстовое поле
answer_entry.place(x=100, y=300)                                                 #   |
number1 = tk.Label(window, text="Введите первое число:")                         #   |  Текст без поля, не для ввода данных
number1.place(x=100, y=50)                                                       #   |
number2 = tk.Label(window, text="Введите второе число:")                         #   |
number2.place(x=100, y=125)                                                      #   |
answer = tk.Label(window, text="Ответ:")                                         #   |
answer.place(x=100, y=275)                                                       #   |
window.mainloop()                                                                #   |->   #Обновление событий, цикл


#(создание кнопки) button_add = tk.Button(переменная из библиотеки) (window (где находится кнопка),
# text="+"(текст кнопки), width=2(ширина), height=2(высота), command=add(что выполняет кнопка))
                    # Запуск приложения без Python
# Terminal (слева внизу у командной строки) ввести команду (' pip install auto-py-to-exe '- для установки плагина)
# auto-py-to-exe для запуска - на сайте выбрать файл и конвертировать в .exe