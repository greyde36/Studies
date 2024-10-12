import tkinter as tk

def test():
    if '-' == button_1_1:
        button_1_1 = tk.Button(window, text='X', width=2, height=2)
        button_1_1.place(x=100, y=70)
    else:
        number2 = tk.Label(window, text='Ячейка занята')
        number2.place(x=100, y=20)

# for turn in range(1, 10):
#     if turn % 2 == 0:
#         turn_char = '0'
#         print('Ходят нолики')
#     else:
#         turn_char = 'X'
#     print(f'Ход: {turn_char}')

window = tk.Tk()
window.title('Крестики-нолики')
window.geometry("350x350")
window.resizable(False, False)
window['bg']='blue'
button_1_1 = tk.Button(window, text="-", width=2, height=2, command=test)
button_1_1.place(x=100, y=70)
button_1_2 = tk.Button(window, text="-", width=2, height=2)
button_1_2.place(x=150, y=70)
button_1_3 = tk.Button(window, text="-", width=2, height=2)
button_1_3.place(x=200, y=70)
button_2_1 = tk.Button(window, text="-", width=2, height=2)
button_2_1.place(x=100, y=120)
button_2_2 = tk.Button(window, text="-", width=2, height=2)
button_2_2.place(x=150, y=120)
button_2_3 = tk.Button(window, text="-", width=2, height=2)
button_2_3.place(x=200, y=120)
button_3_1 = tk.Button(window, text="-", width=2, height=2)
button_3_1.place(x=100, y=170)
button_3_2 = tk.Button(window, text="-", width=2, height=2)
button_3_2.place(x=150, y=170)
button_3_3 = tk.Button(window, text="-", width=2, height=2)
button_3_3.place(x=200, y=170)
number2 = tk.Label(window, text='#чей ход')
number2.place(x=100, y=20)
number2 = tk.Label(window, text="#кто победил")
number2.place(x=100, y=325)
window.mainloop()



                    # Запуск приложения без Python
# Terminal (слева внизу у командной строки) ввести команду (' pip install auto-py-to-exe '- для установки плагина)
# auto-py-to-exe для запуска - на сайте выбрать файл и конвертировать в .exe