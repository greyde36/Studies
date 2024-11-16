def Lucky_SPB(ticket):
    if sum(int(i) for i in ticket[0::2]) == sum(int(x) for x in ticket[1::2]):
        print('Билет счастливый')
        return True
    else:
        print('Билет не счастливый')
        return False


if __name__ == "__main__":
    #Lucky_SPB(input("Введите номер вашего билета: "))
    Lucky_SPB('12344321')
    Lucky_SPB('12341234')
    Lucky_SPB('1234123')