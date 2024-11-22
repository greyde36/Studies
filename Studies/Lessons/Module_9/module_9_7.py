def sum_three(a, b, c):
    return a + b + c


def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result > 1:
            if all(result % i for i in range(2, result)):
                print("Простое")
            else:
                print("Составное")
        else:
            print("Не является числом")

    return wrapper


result = sum_three(3, 5, 7)
print(result)
is_prime(sum_three)(3, 5, 7)