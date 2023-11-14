# my1DList = ["a",5,"b",6,"c",8]
# my2DList = [["an",5],["b",[8,9,10]],["c",8]]

# # print(my2DList[0])


# # myStr = "institute"
# # print(myStr[2])

# print(my2DList[2][1],',', my2DList[0])

# otherVariable = [my1DList[4],my1DList[5]]
# print(otherVariable)



# numbers = [20,21,100,23,240, 50]
# # print(len(numbers))

# largeNumber = 0;
# for i in range(len(numbers)):
#     # print(numbers[i])
#     if(numbers[i]>largeNumber):
#         largeNumber = numbers[i]
        
# print(largeNumber)




# my2DList = [["x",40], ["y",50,60], ["z",23]]

# largeNumber = 0
# for i in range(len(my2DList)):
#     # print(my2DList[i][1])
#     if((my2DList[i][1]>largeNumber)):
#         largeNumber = my2DList[i][1]


# print(largeNumber)


# for j in range(3):    
#     nums = [1, 2, 5, 6, 8]
#     userInput = int(input("enter a number : "))
#     print(userInput)

#     flag = 0
#     for i in range(len(nums)):
#         if(userInput == nums[i]):
#             flag = 100
            
#     if(flag == 100):
#         print("yes")
#     else:
#         print("no")

# for j in range(4):
#     numbers = [5,6,7,8,11,12,44,99]
#     userInput = int(input("enter a number : "))
#     print(userInput)

#     flag = 0
#     for i in range(len(numbers)):
#          if(userInput==numbers[i]):
#               flag = 100
        
#     if (flag == 100):
#             print("yes")
#     else:
#             print("no")
# # my2DList = [["x",40], ["y",50], ["z",23]]

# largeNumber = 0
# for i in range(len(my2DList)):
#     # print(my2DList[i][1])
#     if((my2DList[i][1]>largeNumber)):
#         largeNumber = my2DList[i][1]


# print(largeNumber)


# my2DList = [["n",60],["m",50],["o",90]]

# largeNumber = 0
# for i in range(len(my2DList)):
#     if((my2DList[i][1])>largeNumber):
#         largeNumber = my2DList[i][1]
        
# print(largeNumber)


userDB = [
    ['111', 1111, 1000],
    ['222', 2222, 2000],
    ['333', 3333, 3000],
    ['444', 4444, 4000],
    ['555', 5555, 5000],
]
userInput = input("enter your card number : ")

flag = 0
for i in range(len(userDB)):
    if((userDB[i][1])==userInput):
        print("yes")
        flag = 1
        break
if(flag==0):
    print("no")
        