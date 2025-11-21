# src = "aaaabbb"

# output = ""

# count = 1
# if src != "":              
     
#     for i in range(1, len(src)):
#         if src[i] == src[i - 1]:
#             count += 1
#         else:
#             output = output + src[i - 1] + str(count)
#             count = 1
#     output = output + src[-1] + str(count)

# print(f"src = '{src}'")
# print(f"output = '{output}'")

src = input("Enter a string: ").strip()

output = ""
if src != "":           
    count = 1
    for i in range(1, len(src)):
        if src[i] == src[i - 1]:
            count += 1
        else:
            output = output + src[i - 1] + str(count)
            count = 1
    output = output + src[-1] + str(count)

print(f"src = '{src}'")
print(f"output = '{output}'")
