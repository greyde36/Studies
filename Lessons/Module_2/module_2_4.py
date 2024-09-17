numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = numbers
for i in numbers:
    for j in range(2, i + 1 // 2):
        if i % j == 0:
            not_primes.append(i)
            break
for i in numbers[1:16]:
    if i not in not_primes:
        primes.append(i)
print('Prime', primes)
print('Not prime', list(set(not_primes)))