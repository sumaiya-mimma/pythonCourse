                                  #exercise module 1
#print
#1
print(r"c:\some\ages")
print(r"c:\some\name")
print(r"c:\some\text")


print(3*('un'+'ium'))

userInput = input("enter a list of number seperated by comma(,):")
userList = userInput.split(",")
#userTuple = tuple(userList)
print(userList)#print(userTuple)
myNumberList = []
i = 0
while i<len(userList):
    myNumberList.append(int(userList[i]))
    i = i+1
    print(myNumberList)

