import random

def coin(n):
    head = 0
    tail = 0

    for a in range(n):
        toss = random.randint(0, 1)
        if toss == 0:
            head += 1
        else:
            tail += 1

    print(f"{n} coin flips performed")
    print(f"Probability of heads: {head / n:.4f}")
    print(f"Probability of tails: {tail / n:.4f}")

num = int(input("How many times you want to toss the coin? "))
coin(num)

