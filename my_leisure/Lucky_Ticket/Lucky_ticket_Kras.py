def Lucky_KRD(ticket):
    if sum(int(i) for i in ticket[0:3]) == sum(int(i) for i in ticket[-3:]):
        print('Билет счастливый')
        return True
    else:
        print('Билет не счастливый')
        return False


if __name__ == "__main__":
    #Lucky_KRD(input("Введите номер вашего билета: "))
    Lucky_KRD('12344321')
    Lucky_KRD('12341234')
    Lucky_KRD('1234123')