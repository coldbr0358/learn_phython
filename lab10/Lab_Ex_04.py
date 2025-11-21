menu = {"Americano" : "3,000 won",
        "Ice Americano" : "3,500 won",
        "Cappuccino" : "4,000 won",
        "Cafe Latte" : "4,500 won",
        "Espresso" : "3,600 won"}

for k in menu:
    print(f"{k}\tPrice: {menu[k]}")

order = input("Please select one of the menus above: ")
cnt = 0

for k, v in menu.items():
    if order.lower() == k.lower():
        print(f"{k} is {v}. Please pay.")
        cnt = 1
            
if cnt == 0:
    print(f"Sorry, {order} is not in the menu")
