# my_dic= {"name" : "John", "age":20,"=grade":90}

# print("size of dictioknary: ", len(my_dic))

# print("my first dictionary: ", my_dic)


# d = { 1 : 2, False : 20, (1, 2) : "튜플" }
# d.update({1:3, False:"불린값", (1,2):[1,2],
#           "key":"value" })
# print(d[1])
# print(d[False])
# print(d[(1,2)])
# print(d["key"])

# my_dic = {"name": "Jhon", "age": 20, "grade": 90}

# my_tuple = (1,2,[3,4])
# my_tuple[2][0]=7

# print("my tuple: ", my_tuple)

# fruits_dic = {"apple":6000, "melon" : 3000, "banana":5000, "orange" : 7000}

# print(fruits_dic.keys())
# print(fruits_dic.values())
# fruits_dic.pop("apple")
# print(fruits_dic)
# fruits_dic.clear()
# print(fruits_dic)


# s1 = {1,3,4}
# s2 = set([1,2,3])

# print("set from list: ", s2)

# s3 = set((1,2,3))
# print("set from tuple: ", s3)

# char_set = set("hello")
# char_set.add(3)
# char_set.update("friend")
# print("Char set: ", char_set)

###########################
# s1 = {10,20,30,40}
# s2 = {30,4050,60,70}

# #1)
# print(s1 | s2)
# #2)
# print(s1 & s2)
# #3)
# print(s1 - s2)
# #4)
# print(s1^s2)
# #5)
# print(s1.issubset(s2))

##############################

# import random

# nums = set()

# while len(nums) < 10:
#     r = random.randint(1, 20)
#     nums.add(r) 

# print(nums)

import random

nums = [] 

while len(nums) < 10:
    r = random.randint(1, 20)
    if r not in nums: 
        nums.append(r)

print(nums)

