

tup = (1, 2, 5, 4, 3, 2, 9, 1, 4, 7, 8, 9, 9)
dup = []               

for i in tup:
    if tup.count(i) > 1 and i not in dup:   
        dup.append(i)

print("Original tuple:", tup)
print("Duplicated elements:", dup)
