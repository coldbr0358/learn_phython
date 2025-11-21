with open("C:\\Temp\\coord.txt", "r") as file:
    N = int(file.readline().strip())
    result = []

    for i in range(N):
        x,y = map(int, file.readline().split())
        result.append((x,y))

for i in range(N - 1):
    for j in range(N - i - 1):
        tmp1 = result[j]
        tmp2 = result[j+1]

        if tmp1[0] > tmp2[0]:
            result[j], result[j+1] = result[j+1], result[j]

        elif tmp1[0] == tmp2[0] and tmp1[1] > tmp2[1]:
            result[j], result[j+1] = result[j+1], result[j]

print("Sorted points: ")
for x,y in result:
    print(x, y)