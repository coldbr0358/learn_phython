print("Welcome to Python Restaurant!!!")
print("- Burger (b)")
print("- Chicken (c)")
print("- Pizza (p)")

while True:
    i = input("Please select a menu item: ").strip()
    i = i[:1].lower()
    
    if i != 'b' and i != 'c' and i != 'p':
        i = input("Please select a menu item: ").lower()
        i = i[:1].lower()

    else:
        break
 

if i == 'b':
    print("You have selected burger.")
elif i == 'c':
    print("You have selected chiken.")
elif i == 'p':
    print("You have selected pizza.")