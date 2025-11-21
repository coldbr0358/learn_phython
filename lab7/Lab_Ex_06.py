
# def sorting(n,idx):
#     for i in range(-1,0,-1):
#         result[idx*2] = n
#     return result


# n = input("Enter an integer: ").strip()
# result = {0}
# idx = len(n)/2

# if (len(n)/2) != 2:
#     print(f"{n} is not a palindrome number.2")
#     exit()


# if n == sorting(n,idx):
#     print(f"{n} is a palindrome number.")
# else:
#     print(f"{n} is not a palindrome number.")


num = input("Enter an integer: ")
cnt = 0

for i in range(len(num) // 2):
    if num[i] != num[len(num) - i - 1]:
        cnt = 1
        break

if cnt == 1:
    print("%s is not a palindrome number." % num)
else:
    print("%s is a palindrome number." % num)
