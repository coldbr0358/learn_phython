
tup = tuple(map(int, input("Enter the elements of the tuple separated by spaces: ").split()))

for i in range(len(tup)):
    print(tup[:len(tup) - i])
