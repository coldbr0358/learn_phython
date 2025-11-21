import random

n1 = set()

while True:
    c = random.randint(1,20)
    if c not in n1:
        n1.add(c)
    if len(n1) == 10:
        break
print(n1)

n2 = []

while True:
    c2 = random.randint(1,20)
    if n2.count(c2) == 0:
        n2.append(c2)
    if len(n2) == 10:
        break
print(n2)