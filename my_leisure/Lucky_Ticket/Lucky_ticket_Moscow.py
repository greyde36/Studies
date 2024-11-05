def Lucky_MSC(ticket):
    if len(str(ticket)) % 2 != 0:                   # Если поменять условия можно сократить код убрав лишние переменные
        print('Билет не считаем')
        quit()
    # l_ticket = []
    # while ticket > 0:
    #     l_ticket.append(ticket % 10)
    #     ticket //= 10
    # l_ticket.reverse()
    l_ticket = [i for i in ticket]                  # Альтернатива while # разбивает на числа в список l_ticket но оставляет тип str
    part1 = []
    for i in range(0, len(l_ticket) // 2):
        part1.append(int(l_ticket[i]))              # меняем цифры с типа str на int
    part2 = []
    for i in range(len(l_ticket) // 2, len(l_ticket)):
        part2.append(int(l_ticket[i]))              # меняем цифры с типа str на int
    if sum(part1) == sum(part2):
        print('Билет счастливый')
    else:
        print('Билет несчастливый')


if __name__ == "__main__":
    Lucky_MSC(input("Введите номер вашего билет: "))