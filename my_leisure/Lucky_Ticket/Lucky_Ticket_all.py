from Lucky_ticket_Moscow import Lucky_MSC as LMSC
from Lucky_ticket_Kras import Lucky_KRD as LKRD
from Lucky_ticket_Piter import Lucky_SPB as LSPB


def Mega_Lucky(ticket):
    result = [LMSC, LKRD, LKRD]
    if all(result):
        print(result)
        print('Пора в казино за большим кушем, билет счастливый по всем методам!')
    else:
        LMSC(ticket)
        LKRD(ticket)
        LSPB(ticket)


Mega_Lucky(input("Введите номер вашего билета: "))
# функции возвращают 16-ричный код вместо True