numbers = [10, 20, 5, 8, 30]
max = numbers[0]
min = numbers[0]
for num in numbers:
    if num > max:
        maxi = num
    if num < min:
        min = num
print("Maximum:", max)
print("Minimum:", min)