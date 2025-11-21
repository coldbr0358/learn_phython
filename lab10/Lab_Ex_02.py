tup = ( 1, 2, 5, 4, 3, 2, 1, 4, 7, 8, 9, 9, 3, 7, 3)

print(f"Given tuple:  {tup}")

res = set(tup)
res = tuple(res)

print(f"Tuple with duplicates removes:  {res}")