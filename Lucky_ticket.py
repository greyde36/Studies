ticket=int(input('Введите номер билета: '))
if len(str(ticket))%2!=0:
    print('Билет не считаем (неудачный)')
    quit()
l_ticket=[]
while ticket>0:
    l_ticket.append(ticket%10)
    ticket//=10
l_ticket.reverse()
part1=[]
for i in range(0, len(l_ticket)//2):
    part1.append(l_ticket[i])
part2=[]
for i in range(len(l_ticket)//2, len(l_ticket)):
    part2.append(l_ticket[i])
print(sum(part1))
print(sum(part2))