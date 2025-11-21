# num = int(input("Enter 5 numbers: ").replace(","," "))

# sum = 0
# for i in range(5):
#     sum += num[i]
# print(f"Sum : {sum}")

# avg = sum / 5
# print(f"Average : {avg}")

# max = num[0]
# for i in range(5):
#     if max < num[i]:
#         max = num[i]

# for i in range(5):
#     if min > num[i]:
#         min = num[i]
# print(f"Maximum value : {max}")
# print(f"Minimum value : {min}")


nums = input("Enter 5 numbers: ").split(',')

numbers = []

for n in nums:
    numbers.append(int(n))

total = sum(numbers)
avg = total / len(numbers)
max_val = max(numbers)
min_val = min(numbers)

print("Sum:", total)
print("Average:", avg)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
