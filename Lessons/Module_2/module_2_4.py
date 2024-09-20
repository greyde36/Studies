# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# primes = []
# not_primes = []
# for i in numbers[1:]:
#     if i%2==0 and i//2!=1 or i%3==0 and i//3!=1 or i%5==0 and i//5!=1 or i%7==0 and i//7!=1:
#         not_primes.append(i)
#         continue
#     else:
#         primes.append(i)
# print('Prime', list(set(primes)))
# print('Not prime', list(set(not_primes)))
##################################################################################################
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers[1:]:
    is_prime=True
    for j in range(2,i):
        if i%j==0:
            is_prime=False
            break
    if is_prime:
        primes.append(i)
    else:
        not_primes.append(i)
print(primes)
print(not_primes)