from Lucky_ticket_Moscow import Lucky_MSC as LMSC
from Lucky_ticket_Kras import Lucky_KRD as LKRD
from Lucky_ticket_Piter import Lucky_SPB as LSPB


def Mega_Lucky(ticket):
    if LMSC(ticket) == True and LKRD(ticket) == True and LSPB(ticket) == True:
        print('Пора в казино за большим кушем, билет счастливый по всем методам!')


Mega_Lucky(input("Введите номер вашего билета: "))
