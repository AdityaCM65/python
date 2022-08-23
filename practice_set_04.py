# Practice Set - 4

# # 1) Write a program to store seven fruits in a list entered by the user.
# ->
# f1 = input("Enter Fruit 1 : ")
# f2 = input("Enter Fruit 2 : ")
# f3 = input("Enter Fruit 3 : ")
# f4 = input("Enter Fruit 4 : ")
# f5 = input("Enter Fruit 5 : ")
# f6 = input("Enter Fruit 6 : ")
# f7 = input("Enter Fruit 7 : ")

# myFruitList = [f1 , f2 , f3 , f4 , f5 , f6 , f7]
# print(myFruitList)

# # 2) Write a program to accerpt marks of a 6 Students and display them in a sorted manner.
# # ->
# m1 = int(input("Enter Student 1 Marks : "))
# m2 = int(input("Enter Student 2 Marks : "))
# m3 = int(input("Enter Student 3 Marks : "))
# m4 = int(input("Enter Student 4 Marks : "))
# m5 = int(input("Enter Student 5 Marks : "))
# m6 = int(input("Enter Student 6 Marks : "))

# stdMarksList = [m1 , m2 , m3 , m4 , m5 , m6 ]
# stdMarksList.sort()
# print(stdMarksList)

# # 3) Check that a tuple cannot be changed in python.
# # ->
# tpl = ( 1, 2, 4 , 5)
# tpl[0] = 45
# print(tpl[0])

# # 4) Write a program to sum a list with 4 numbers.
# # -> 
# n1 = int(input("Enter a Number : "))
# n2 = int(input("Enter a Number : "))
# n3 = int(input("Enter a Number : "))
# n4 = int(input("Enter a Number : "))

# numbers = [n1 , n2 , n3 , n4]

# print(numbers[0] + numbers[1] + numbers[2] + numbers[3])
# # or
# print(sum(numbers))

# # 5) Write a program to count the number of zeros in the following tuple.
# # tpl = ( 7 , 0 , 8 , 0 , 0 , 9 )
# # ->
# tpl = ( 7 , 0 , 8 , 0 , 0 , 9 )
# print(tpl.count(0))

# List & Tuples

# List : python list are container to store a set of values of any data type (ordered list)

# friends = ["Aditya" , "Kalpesh" , "Lalit" , "Chetan" , 1, False]
# print(friends)

# # List-Indexing : A list can be indexed like a string
# l1 = [5 , 6 , 8 , 2 ]
# print(l1[2:4])
# print(l1[0:])
# print(l1[:4])
# print(l1[:])

# List-Methods :
l1 = [1 , 5 , 7 , 3 , 9]

# # 1) sort() - used to sort list elements in ascending order or descending order.
# l1.sort()
# print(l1)
# l1.sort(reverse=True)
# print(l1)

# # 2) reverse() - used to reverse a list elements.
# l1.reverse()
# print(l1)

# # 3) append() - used to add element in list at the end.
# l1.append([4 , 3 , 6 ])
# print(l1)

# # 4) insert() - used to add element at specific index postition.
# l1.insert(1,80)
# print(l1)

# # 5) pop() - used to delete a element and return it , when we not pass argument , it delete last element or we pass index number.
# l1.pop()
# l1.pop(1)
# print(l1)

# # 6) remove() - used to remove the value.
# l1.remove(7)
# print(l1)

# Tuples : A Tuple is an immutable ( cannot change ) data type in python.
# a = () # Empty Tuple
# print(type(a))
# b = (1) # Wrong way to implement tuple with single value
# b = (1,) # Right way to implement tuple with single value
# print(type(b))
# c = (1 , 7 , 2) # tuple with more than one element

# Note - once defined a tuple element cant be altered or manipulated

# # Tuple-Methods :
# a = (1 , 7 , 2)

# # 1) count() - used to find total number of occurance of given character.
# print(a.count(1))

# # 2) index() - it will match first occurence and return index of it.
# print(a.index(7))


