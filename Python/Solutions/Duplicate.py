
numbers = [1, 2, 2, 3, 4, 4, 5]
dup = []
for num in numbers:
    if num not in dup:
        dup.append(num)
print("duplicates values :", dup)