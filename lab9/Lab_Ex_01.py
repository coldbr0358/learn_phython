# (1) permission error

try:
    with  open("C:\\Temp\\Py_examples\\my_hello.txt", "w+t") as f:
        f.write(input("Enter txt:"))
    print("good")

except Exception as e:
    print("Error: ",e)
