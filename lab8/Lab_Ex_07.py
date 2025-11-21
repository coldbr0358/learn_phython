def cal(n):
    result = []
    for i in range(1,n+1):
        if n % i == 0:
            result.append(i)
    return result



n = int(input("Enter an integer less than or equal to 1000: "))

result = cal(n)
sumup = sum(result)

print(result)
print(sumup)