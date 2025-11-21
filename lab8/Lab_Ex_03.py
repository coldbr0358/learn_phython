
nums = input("Enter integers separated by spaces: ").split(' ')

numbers = []

for n in nums:
    numbers.append(int(n))

total = sum(numbers)
ave = total / len(numbers)


tmp = 0
for i in numbers:
        tmp += (i-ave)**2

tmp2 = tmp / len(numbers)
stand_devi = tmp2**0.5

print(f"Total sum: {total}")
print(f"Average (mean): {ave:.2f}")
print(f"Standard deviation: {stand_devi:.2f}")
