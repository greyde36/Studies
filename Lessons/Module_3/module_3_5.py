def get_multiplied_digits(number):
    if number == 0:
        return 0
    str_number = str(number)
    first = int(str_number[0])
    if not len(str_number) > 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(40203))
print(get_multiplied_digits(340005723))