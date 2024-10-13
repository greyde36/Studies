my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
numb = []
while True:
    if my_list[0] >= 0:
        numb.append(my_list[0])
        my_list.pop(0)
    else:
        print(numb)
        break
