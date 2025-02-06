List_theory:
What is a List in Python?
- A list is a collection of items that can be of any data type, including strings, integers, floats, and other lists.
- Lists are denoted by square brackets [].
- Lists are mutable, meaning they can be modified after creation.

Creating a List
- my_list = [1, 2, 3, 4, 5]
- my_list = list((1, 2, 3, 4, 5))
- my_list = [i for i in range(1, 6)]

List Methods
1. append(): Add an element to the end of the list.
    - my_list = [1, 2, 3]
    - my_list.append(4)
    - print(my_list)  # Output: [1, 2, 3, 4]

2. extend(): Add multiple elements to the end of the list.
    - my_list = [1, 2, 3]
    - my_list.extend([4, 5, 6])
    - print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

3. insert(): Insert an element at a specified position.
    - my_list = [1, 2, 3]
    - my_list.insert(1, 4)
    - print(my_list)  # Output: [1, 4, 2, 3]

4. remove(): Remove the first occurrence of an element.
    - my_list = [1, 2, 3, 2, 4]
    - my_list.remove(2)
    - print(my_list)  # Output: [1, 3, 2, 4]

5. pop(): Remove and return an element at a specified position.
    - my_list = [1, 2, 3, 4, 5]
    - print(my_list.pop(2))  # Output: 3
    - print(my_list)  # Output: [1, 2, 4, 5]

6. index(): Return the index of the first occurrence of an element.
    - my_list = [1, 2, 3, 2, 4]
    - print(my_list.index(2))  # Output: 1

7. count(): Return the number of occurrences of an element.
    - my_list = [1, 2, 3, 2, 4]
    - print(my_list.count(2))  # Output: 2

8. sort(): Sort the list in-place.
    - my_list = [4, 2, 1, 3]
    - my_list.sort()
    - print(my_list)  # Output: [1, 2, 3, 4]

9. reverse(): Reverse the list in-place.
    - my_list = [1, 2, 3, 4]
    - my_list.reverse()
    - print(my_list)  # Output: [4, 3, 2, 1]

10. copy(): Return a shallow copy of the list.
    - my_list = [1, 2, 3]
    - new_list = my_list.copy()
    - print(new_list)  # Output: [1, 2, 3]

11. clear(): Remove all elements from the list.
    - my_list = [1, 2, 3]
    - my_list.clear()
    - print(my_list)  # Output: []

Important Observations
- Lists are mutable, meaning they can be modified after creation.
- Lists can contain duplicate values.
- Lists maintain the order of elements.
- Indexing starts at 0.

List practise questions:

1.sum of numbers:
num= [1, 2, 3, 4, 5]
sum = 0
for num in numbers:
    sum += num
print("Sum of elements:", total)
--------------------
2.Find the Maximum and Minimum Elements in a List 

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
------------------------------
3. Find the Second Largest Element in a List 

num = [10, 20, 4, 45, 99]
largest = s_largest = num[0]  
for n in num[1:]:
    if n > largest:
        s_largest, largest = largest, num
    elif n > s_largest and n!= largest:
        s_largest = n
print("Second Largest Element:", s_largest)
---------------------
4. Remove Duplicates from a List

numbers = [1, 2, 2, 3, 4, 4, 5]
dup = []
for num in numbers:
    if num not in dup:
        dup.append(num)
print("duplicates values :", dup)
-------------------
5.Find the Intersection of Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
list = []
for num in list1:
    if num in list2 and num not in list:
        list.append(num)
print("result:", list)
---------------------------------------------

6. Find the Union of Two Lists

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
-----------------------------------------
7. Find the Difference Between Two Lists

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
difference = []
for item in list1:
    if item not in list2:
        difference.append(item)
print("Difference of two lists:", difference)




