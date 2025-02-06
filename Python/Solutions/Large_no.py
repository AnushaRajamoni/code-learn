
num = [10, 20, 4, 45, 99]
largest =  0  
for n in num[1:]:
    if n > largest:
        s_largest, largest = largest, num
    elif n > s_largest and n!= largest:
        s_largest = n
print("Second Largest Element:", s_largest)