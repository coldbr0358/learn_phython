linenum = 1
found = False
name = input("Enter the file name: ")
word = input("Enter the word to search for: ")

with open("C:\\Temp\\Py_examples\\"+name,"r") as f:
    for i in f:
        if word in f:
            found = True
            print(f"{linenum}:{i}")
        linenum +=1

if found == False:
    print("That word is not in the file")