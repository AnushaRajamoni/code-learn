
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = []
for item in list1:
    if item not in list2:
        difference.append(item)
print("Difference of two lists:", difference)