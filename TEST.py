def send_email(message, recipient, *, sender='university.help@gmail.com'):
    print(recipient not in '@' and ('.com' or '.ru' or '.net'))
    if recipient:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
        return
    else:
        print('Соси писос')


send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')


