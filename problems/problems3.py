# 1. Write a Python function that takes a sequence of numbers and determines 
#    whether all the numbers are different from each other
# 2. Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', 
# and 'I'. Ensure that each character is used only once.
# 3. Write a Python program that removes and prints every third
# number from a list of numbers until the list is empty.
# 4. Write a Python program to identify unique triplets whose three elements 
# sum to zero from an array of n integers.
# 5. Write a Python program to make combinations of 3 digits.
# 6. Write a Python program that prints long text, converts it to a list, 
# and prints all the words and the frequency of each word.
# 7. Write a Python program to count the number of each character in a text file.
# 8. Write a Python program that retrieves the top stories from Google News.
# 9. Write a Python program to get a list of locally installed Python modules.
# 10. Write a Python program to display some information about the OS where the script is running.
# 11. Write a Python program to check the sum of three elements (each from an array) 
# from three arrays is equal to a target value. Print all those three-element combinations.
# Sample data:
# /*
# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# target = 70
# */
# 12. Write a Python program that generates a list of all possible permutations 
# from a given collection of distinct numbers.
# 13. Write a Python program to get all possible two-digit letter combinations from a 1-9 digit string.
# string_maps = {
# "1": "abc",
# "2": "def",
# "3": "ghi",
# "4": "jkl",
# "5": "mno",
# "6": "pqrs",
# "7": "tuv",
# "8": "wxy",
# "9": "z"
# }
# 14. Write a Python program to add two positive integers without using the '+' operator.
# Note: Use bit wise operations to add two numbers.
# 15. Write a Python program to check the priority of the four operators (+, -, *, /).

# 16. Write a Python program to get the third side of a right-angled triangle from two given sides.
# 17. Write a Python program to get all strobogrammatic numbers that are of length n.
# A strobogrammatic number is a number whose numeral is rotationally symmetric, 
# so that it appears the same when rotated 180 degrees. In other words, 
# the numeral looks the same right-side up and upside down (e.g., 69, 96, 1001).
# For example,
# Given n = 2, return ["11", "69", "88", "96"].
# Given n = 3, return ['818', '111', '916', '619', '808', '101', '906', '609', '888', '181', '986', '689']


# 18. Write a Python program to find the median among three given numbers.


# 19. Write a Python program that finds the value of n when n degrees of number 2 are written sequentially on a line without spaces between them.


# 20. Write a Python program to find the number of zeros at the end of a factorial of a given positive number.
# Range of the number(n): (1 <= n <= 2*109).
# 21. Write a Python program to find the number of notes (Samples of notes: 10, 20, 50, 100, 200, 500) against an amount.
# Range - Number of notes(n) : n (1 <= n <= 1000000).
# 22. Write a Python program to create a sequence where the first four members of
# the sequence are equal to one. Each successive term of the sequence is equal 
# to the sum of the four previous ones. Find the Nth member of the sequence.
# 23. Write a Python program that accepts a positive number and subtracts 
# from it the sum of its digits, and so on. Continue this operation until the number is positive.
# 24. Write a Python program to find the total number of even or odd divisors of a given integer.
# 25. Write a Python program to find the digits that are missing from a given mobile number.
# 26. Write a Python program to compute the summation of the absolute 
# difference of all distinct pairs in a given array (non-decreasing order).
# Sample array: [1, 2, 3]
# Then all the distinct pairs will be:
# 1 2
# 1 3
# 2 3
# 27. Write a Python program to find the type of the progression 
# (arithmetic progression / geometric progression) and the next successive member of the 
# three successive members of a sequence.
# According to Wikipedia, an arithmetic progression (AP) is a sequence of numbers 
# such that the difference of any two successive members of the sequence is a constant. 
# For instance, the sequence 3, 5, 7, 9, 11, 13, . . . is an arithmetic progression 
# with common difference 2. For this problem, we will limit ourselves to arithmetic 
# progression whose common difference is a non-zero integer.
# On the other hand, a geometric progression (GP) is a sequence of numbers 
# where each term after the first is found by multiplying the previous one by a fixed non-zero number 
# called the common ratio. For example, the sequence 2, 6, 18, 54, . . . is a geometric progression 
# with common ratio 3. For this problem, we will limit ourselves to geometric progression 
# whose common ratio is a non-zero integer.
# 28. Write a Python program to print the length of the series and 
# the series from the given 3rd term, 3rd last term and the sum of a series.
# Sample Data:n
# Input third term of the series: 3
# Input 3rd last term: 3
# Input Sum of the series: 15
# Length of the series: 5
# Series:
# 1 2 3 4 5
# 29. Write a Python program to 
# find common divisors between two numbers in a given pair.
# 30. Write a Python program to reverse the digits of a given number 
# and add them to the original. Repeat this procedure if the sum is not a palindrome.
# Note: A palindrome is a word, number, or other sequence of 
# characters which reads the same backward as forward, such as madam or racecar.



# from sqlite3 import Row


# myList1 = []
# userNumbers = input("enter a list of numbers:")
# userList = userNumbers.split(",")
# for i in range(len(userList)):
# # i = 0
# # while i<len(userList1):
#     myList1.append(int(userList[i]))
#     # i = i + 1
#     print(userList)
    
# myList2 = []
# userNumbers1 = input("enter a list of numbers: ")
# userList1 = userNumbers1.split(",")
# for i in range(len(userList)):
#     myList2.append(int(userList1[i]))
#     print(userList1)
    
#     if userList[i]!=userList1[i]:
#         print("true")
#     else:
#         print("false")
        
        
        
# 3. Write a Python program that removes and prints every third number 
# from a list of numbers until the list is empty.

# i = 0
# while i<myList:
# myList = []
# arrLen = int(input("how many numbers have you got:"))
# if arrLen>0:
#     print(arrLen)
#     for i in range(arrLen):
#         numbers = int(input("enter your list of numbers:"))
#         myList.append(numbers)
#         print(myList)
# for i in range(len(myList)):
#  print(myList[2])
#  myList[2]=[]
#  print(myList)

    
# def digitCombo():
#     combinations = []
#     for i in range(10):
#         for j in range(10):
#             for k in range(10):
#                 combination = i * 10 + j * 10 + k * 10
#                 combinations.append(combination)
#     return combinations
            
# result = digitCombo()
# print(result)


# import platform

# def displayOsInfo():
    
#     systemName = platform.system()
#     systemRelease = platform.release()
#     systemVersion = platform.version()
#     machineType = platform.machine()
#     processor = platform.processor()
    
    
#     print(f"System: {systemName}")
#     print(f"Release: {systemRelease}")
#     print(f"Version: {systemVersion}")
#     print(f"Machine Type: {machineType}")
#     print(f"Processor: {processor}")

    
# displayOsInfo()


# X = [10, 20, 20, 20]
# Y = [10, 20, 30, 40]
# Z = [10, 30, 40, 20]
# target = 70
# def threeDigitsCombo(X,Y,Z, target):
#     result = []
#     for x in X:
#         for y in Y:
#             for z in Z:
#                 if x + y + z == target:
#                     result.append(x,y,z)
            
#             return result
#         print(result)
# combinations = threeDigitsCombo(X,Y,Z,target)

# # for combination in combinations:
# #     print(f"three digits combination sum of{target}: ", combinations)


#12
# numbers = []
# userInput = input("enter a list of numbers:")
# # userNumbers = userInput.split(",")
# for i in range(len(userInput)):
#     numbers.append(userInput[i])
#     # print(numbers)
# from itertools import permutations
# def generatePermutations(numbers):
#     permutation = permutations(numbers)
#     permutationList = list(permutation)
#     for permutation in permutationList:
#         print(permutation)
# generatePermutations(numbers)


userInput = input("enter a list of numbers:")
userList = userInput.split(",")
print(userList)
