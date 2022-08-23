# Practice Set : Chapter 3

# 1) Write a python program to display a user entered name followed by good afternoon using input() function.
# -> 
# name = input("Enter Your Name : \n")
# print("Good Afternoon, "+name)
# print("Good Afternoon, ",name)

# 2) Write a program to fill in a letter template given below with name and date.
# ->
# letter = '''Dear <|Name|>
#             You are Selected!
#             Date : <|Date|>'''

# name = input("Enter Your Name : ")
# date = input("Enter Date : ")


# letter = letter.replace("<|Name|>" , name)
# letter = letter.replace("<|Date|>" , date)

# print(letter)

# 3) Write a program to detect double spaces in a string.
# ->
# string = "This is  a  String"
# double_spaces = string.find("  ")
# print(double_spaces)

# 4) Replace the double spaces from problem no 3 with single spaces.
# ->
# string = "This is  a  String"
# result = string.replace("  " , " ")
# print(result)

# 5) Write a program to format the following letter using escape sequence characters.
# letter - "Dear Aditya, This python course is nice. Thanks!"
# ->
# letter = "Dear Aditya,\n This python course is nice. \n\tThanks!"
# print(letter)

# # Practicing String Functions : 
# name = "Aditya"

# # len() - used to find length of string.
# print(len(name))

# # endswith() - Matching occurence and return boolean values.
# print(name.endswith("ya"))

# # count() - counts the total number of occurences of any character.
# print(name.count("a"))

# # capitalize() - This function capitalize the first character of given string.
# my_surname = "mahajan"
# print(my_surname.capitalize())

# # find() - This function finds a word or character and returns index no of first occurence otherwise return -1.
# print(my_surname.find("a"))

# # replace() - This function replaces the oldword with newword in the entire string.
# print(name.replace("tya" , "ti"))

# String Slicing :

# name = "Aditya"
# print(name[0])
# print(name[-4:-1])
# print(name[0:])
# print(name[:6])

# String With Skip Value :

# name = "Aditya"
# print(name[0:6:2])

# numbers = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8, 9 , 10]
# print(numbers[0::2]) #odd numbers
# print(numbers[1::2]) #even numbers

# Escape Sequence Characters :

# statement = "My name is 'Aditya'"
# print(statement)
# statement = 'My name is "Aditya"'
# print(statement)
# statement = '''My name is "Aditya" and My age is '20\''''
# print(statement)

# Rather than it Use Escape Characters.
# statement = "My name is \"Aditya\" and My age is \'20\'"
# print(statement)

# Note : String Values can not be assign after define.
# name = "Aditya"
# name[2] = "t"
# print(name[2])


