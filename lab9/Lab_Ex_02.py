print("hello.txt file:")

with open ("C:\\Temp\\Py_examples\\hello.txt","r") as f:
    print(f.read())


with open ("C:\\Temp\\Py_examples\\hello.txt","a") as f:
    f.write("\nWelcome to Python!")

print()
with open ("C:\\Temp\\Py_examples\\hello.txt","r") as f:
    print(f.read())


