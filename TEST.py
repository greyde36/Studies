def send_email(message, recipient, *, sender='university.help@gmail.com'):
    if '@' in recipient and recipient.endswith('com', '.ru', '.net'):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender == recipient:
        print('Нельзя отправлять письмо самому себе')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
    else:
        print('нестандартный отправитель!'.upper(), f'Письмо отправлено с адреса {sender} на адрес {recipient}')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!

#У Вас не происходит вывод правильных сообщений из-за того, что не совсем корректно сформировано условие вывода сообщение о невозможности отправки сообщения.
# Не стоит слишком объединять проверки между собой, попробуйте построить её по следующему шаблону:
# "Если символ @ находится в адресе отправителя ИЛИ символ @ находится в адресе получателя
# ИЛИ адрес отправителя оканчивается на ".com" или ".ru" или ".net" ИЛИ адрес получателя оканчивается на ".com" или ".ru" или ".net""
# А для того, чтобы проверить, чем оканчиваются адреса, лучше использовать метод строки .endswith()/