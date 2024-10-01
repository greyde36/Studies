import tkinter as tk                                                                     # Библиотека

window = tk.Tk()                                                                 #   |->  #Создание окна
window.title('Калькулятор')                                                      #   |  Название окна
window.geometry("350x350")                                                       #   |  Размер окна
window.resizable(False, False)                                       #   |  Запрет на изменения размеров окна
button_add = tk.Button(window, text="+", width=2, height=2, command=add)         #   |  Создать кнопку
button_add.place(x=100, y=200)                                                   #   |  Расположение кнопки по координатам
button_sub = tk.Button(window, text="-", width=2, height=2, command=sub)         #   |
button_sub.place(x=150, y=200)                                                   #   |
button_mul = tk.Button(window, text="*", width=2, height=2, command=mul)         #   |
button_mul.place(x=200, y=200)                                                   #   |
button_div = tk.Button(window, text="/", width=2, height=2, command=div)         #   |
button_div.place(x=250, y=200)                                                   #   |
number1_entry = tk.Entry(window, width=28)                                       #   |
number1_entry.place(x=100, y=75)                                                 #   |
number2_entry = tk.Entry(window, width=28)                                       #   |
number2_entry.place(x=100, y=150)                                                #   |
answer_entry = tk.Entry(window, width=28)                                        #   |
answer_entry.place(x=100, y=300)                                                 #   |
number1 = tk.Label(window, text="Введите первое число:")                         #   |
number1.place(x=100, y=50)                                                       #   |
number2 = tk.Label(window, text="Введите второе число:")                         #   |
number2.place(x=100, y=125)                                                      #   |
answer = tk.Label(window, text="Ответ:")                                         #   |
answer.place(x=100, y=275)                                                       #   |
window.mainloop()                                                                #   |->   #Обновление событий, цикл


#(создание кнопки) button_add = tk.Button(переменная из библиотеки) (window (где находится кнопка),
# text="+"(текст кнопки), width=2(ширина), height=2(высота), command=add)