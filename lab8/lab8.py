# def f(n):
#     list = []
#     for i in range(n):
#         num = int(input("Enter: "))



# n = int(input(" "))

# list = f(n)



# def f(n,t):
#     for i in range(n):
#         t = int(input("Enter integer: "))
    
#     return t

# n = int(input("Enter: "))

# t = f(n.t)


def funcReturnsTuple():
    return 1, 2
def funcReturnsList():
    return [3, 4, 5]
tuple1 = funcReturnsTuple()
list1 = funcReturnsList()
x, y = funcReturnsTuple()
a, b, c = funcReturnsList()

print(tuple1)
print(list1)
print(x)
print(y)
print(a,b,c)
