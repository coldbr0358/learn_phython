
while True:
    n = int(input("Enter a number between 1 and 9:"))
    if n >9 and n<1:
        n = int(input("Enter a number between 1 and 9:"))
    
    elif 1<=n<=9:
        break

for i in range(1,10):
    print(f"{n}*{i}= {n*i}")