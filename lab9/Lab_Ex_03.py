name = input("Enter the file name: ").strip()

try:
    f = open("C:\\Temp\\Py_examples\\"+name, "r")

except FileNotFoundError:
    name = input("there is not such file. Enter again the file name: ")
    f = open("C:\\Temp\\Py_examples\\"+name,"r")

a = f.readlines()

print("\nFile content:")
for i in a:
    print(i.strip())
f.close()