from datetime import datetime

while True:
    try:
        n = input("Enter an integer(1-100): ").strip()
        num = int(n)

        if not (1<= num <= 100):
            raise ValueError("Out of range")
        
        print(f"Valid number entered: {num}")
        break


    except ValueError as e:
        
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open ("C:\\Temp\\error_logs.txt","a") as log:
            log.write(f"[{time}] {n} → {e}\n")
        
        print("Error: ",e, end=" (logged)\n")

print()
print("=== error_logs.txt ===")

with open("C:\\Temp\\error_logs.txt","r") as log:
    print(log.read())
    




