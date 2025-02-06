
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list = []
for num in list1:
    if num in list2 and num not in list:
        list.append(num)
print("result:", list)