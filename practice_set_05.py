# Practice Set - 5

# # 1) Write a program to create a dictionary of hindi words with values as 
# # their english translation , provide user with an option to look it up!
# # ->
# myDict = {
#     "Pankha" : "Fan",
#     "Dabba" : "Box" ,
#     "Vastu" : "Item" ,
#     "Khidki" : "Window"
# }

# print("Options Are : Pankha  , Dabba , Vastu , Khidki ")
# user_word = input("Enter Word : ")
# print(myDict.get(user_word))

# # 2) Write a program to input eight numbers from the user and display all unique numbers (once)
# # ->
# n1 = int(input("Enter Number : "))
# n2 = int(input("Enter Number : "))
# n3 = int(input("Enter Number : "))
# n4 = int(input("Enter Number : "))
# n5 = int(input("Enter Number : "))
# n6 = int(input("Enter Number : "))
# n7 = int(input("Enter Number : "))
# n8 = int(input("Enter Number : "))

# my_set = {n1 , n2 , n3 , n4 , n5 , n6 , n7 , n8}

# print(my_set)

# # 3) Can We have a set with 18(int) and "18"(str) as a value in it ?
# # ->
# s = {18 , "18"}
# print(s)

# # 4) What will be the length of following set s 
# # s = set()
# # s.add(20)
# # s.add(20.0)
# # s.add("20")
# # -> 
# s = set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(s)
# print(len(s))

# # 5) s = {} What is the type of s ?
# # ->
# s = {}
# print(type(s)) #dictionary

# # 6) Create an empty dictionary , allow 4 friends to enter their favourite language as values and use key as their names , Assume that the names are unique.
# # ->
# fav_lang = {}

# a_lang = input("Enter Your Favourite Language Shubham : ")
# b_lang = input("Enter Your Favourite Language Rohit : ")
# c_lang = input("Enter Your Favourite Language Sonu : ")
# d_lang = input("Enter Your Favourite Language Chetan : ")

# fav_lang["shubham"] = a_lang
# fav_lang["rohit"] = b_lang
# fav_lang["sonu"] = c_lang
# fav_lang["chetan"] = d_lang

# print(fav_lang)

# # 7) If names of 2 friends are same , What will happen to the program in problem 6 ?
# # ->
# fav_lang = {}

# a_lang = input("Enter Your Favourite Language Shubham : ")
# b_lang = input("Enter Your Favourite Language Rohit : ")
# c_lang = input("Enter Your Favourite Language Sonu : ")
# d_lang = input("Enter Your Favourite Language Chetan : ")

# fav_lang["shubham"] = a_lang
# fav_lang["rohit"] = b_lang
# fav_lang["shubham"] = c_lang
# fav_lang["chetan"] = d_lang

# print(fav_lang)

# # 8) If Languages of two friends are same what will happen to the program in problem 6 ?
# # ->
# fav_lang = {}

# a_lang = input("Enter Your Favourite Language Shubham : ")
# b_lang = input("Enter Your Favourite Language Rohit : ")
# c_lang = input("Enter Your Favourite Language Sonu : ")
# d_lang = input("Enter Your Favourite Language Chetan : ")

# fav_lang["shubham"] = a_lang
# fav_lang["rohit"] = b_lang
# fav_lang["sonu"] = c_lang
# fav_lang["chetan"] = d_lang

# print(fav_lang)

# # 9) Can you change the values inside a list which is contained in set s.
# #  s = { 8 , 7 , 12 , "ACM" , [1 , 2]}
# # ->
#  s = { 8 , 7 , 12 , "ACM" , [1 , 2]}
#  print(s)


# Dictionary : is a collection of key-value pairs.
# a = {
#     "Aditya" : "Mahajan",
#     "Marks" : 98,
#     "List" : [1 , 2 , 3]
# }

# print(a["Aditya"])
# print(a.get("Aditya"))

# print(a["Kalpesh"]) # if value not found it gives error
# print(a.get("Kalpesh")) # if value not found it return none

# Properties of Dictionaries : 
# 1) It is unordered , 2) It it mutable , 3) It is Indexed , 4) Cannot contain duplicate keys

# # Dictionary-Methods : 
# a = {
#     "name" : "Aditya",
#     "from" : "India",
#     }

# # 1) items() - returns a list of (key, value) in the form of tuple.
# print(a.items())

# # 2) keys() - returns a list of keys containing dictionary.
# print(a.keys())

# # 3) value() -returns a list of values containing dictionary.
# print(a.values())

# # 4) update() - Updates the dictionary with key value pairs.
# a.update({"friend" : "Kalpesh"})
# print(a)

# # 5) get() - returns the value of specified keys and returned the value , if value not found it will be return none.
# print(a.get("name"))


# Sets in Python : is a collection of non-repetitive elements ( containes unique values ).

# s = {1 , 2 , 3}
# print(s)
# s = set()
# print(type(s))
# s.add("India")
# s.add("America")
# s.add("Dubai")
# print(s)

# Properties of a Sets -
# 1) Sets are unordered , 2) Sets are unindexed , 3) There is no way to change items in Sets , 4) Sets cannot contain duplicate values.

# # Operations On Set :
# s = { 1 , 2 , 3 , 4 , 5}

# # 1) len() - returns the length of Set.
# print(len(s))

# # 2) remove() - updates the Set and remove specific element.
# s.remove(2)
# print(s)

# # 3) pop() - Removes an arbitrary element ( random element ) from the set and return that element.
# s.pop()
# print(s)

# # 4) clear() - Empties the Set.
# # s.clear()
# # print(s)

# # 5) union - Returns a new set with all items from both sets.
# s.union()
# print(s)

# # 6) intesection() - Returns a set which contain only items in both set.
# s.intersection({1 , 2})
# print(s)













