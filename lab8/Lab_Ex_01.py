list1 = ['I like', 'I love']
list2 =['pancakes.','kiwi juice.','espresso.']

for i in range(len(list1)):
    for j in range(len(list2)):
        print(f"{list1[i]}", end =" ")
        print(f"{list2[j]}")

for i in list1:
    for j in list2:
        print(i,j)
