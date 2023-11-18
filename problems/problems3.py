# 1. Write a Python function that takes a sequence of numbers and determines 
#    whether all the numbers are different from each other

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


import platform

def displayOsInfo():
    
    systemName = platform.system()
    systemRelease = platform.release()
    systemVersion = platform.version()
    machineType = platform.machine()
    processor = platform.processor()
    
    
    print(f"System: {systemName}")
    print(f"Release: {systemRelease}")
    print(f"Version: {systemVersion}")
    print(f"Machine Type: {machineType}")
    print(f"Processor: {processor}")

    
displayOsInfo()
 