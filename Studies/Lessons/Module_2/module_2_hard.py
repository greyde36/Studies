import random

a = random.randint(3, 20)
b = []
c = []
d = []
for i in range(1, a + 1):
    b.append(i)
    c.append(i)
for i in range(1, len(b)):
    for j in range(1, len(b) + 1):
        if a % (i + j) == 0 and a != j and i < j:
            if j != i:
                d.append(i)
                d.append(j)
            if i > (a / 2):
                break
print(a, '-', d)
