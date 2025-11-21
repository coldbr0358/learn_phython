import math

def cal(tup):
    i = 0
    while i < len(tup):
        shape = tup[i]
        if shape == "rectangle":
            w = tup[i + 1]
            h = tup[i + 2]
            area = w * h
            print(f"{shape}, {w}, {h}, {area}")
            i += 3
        elif shape == "circle":
            r = tup[i + 1]
            area = math.pi * r * r
            print(f"{shape}, {r}, {area}")
            i += 2
        else:
            break


data = ("rectangle", 30, 20,
        "circle", 10,
        "rectangle", 20, 40,
        "rectangle", 10, 10,
        "circle", 20)

cal(data)

