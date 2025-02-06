
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
union = []
for item in list1:
    if item not in union:
        union.append(item)
for item in list2:
    if item not in union:
        union.append(item)
print("Union of the two lists:", union)