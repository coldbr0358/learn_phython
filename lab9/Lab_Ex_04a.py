name1 = input("Enter the name of the first file to link: ").strip()
name2 = input("Enter the name of the second file to link: ").strip()
mer_name = input("Enter the name of the file to save: ").strip()

print("\nThe merged file content is: ")

with open("C:\\Temp\\Py_examples\\"+name1,"r") as f1,\
      open("C:\\Temp\\Py_examples\\"+name2,"r") as f2,\
        open("C:\\Temp\\Py_examples\\"+mer_name,"w") as f3:
    
    tmp1 = f1.read()
    tmp2 = f2.read()
    f3.write(tmp1+"\n"+tmp2)
   

with open("C:\\Temp\\Py_examples\\"+mer_name,"r") as f:
    for i in f:
        print(i.strip())