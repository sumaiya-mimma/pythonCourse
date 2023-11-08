# 
# arr = []
# arrLen = int(input("how many elements you have got:"))
# if(arrLen>=0):
#     print(type(arrLen))
#     for i in range(arrLen):
#         print("enter your elements name:")
#         element = str(input())
#         arr.append(element)
#     print(arr)
#     if(arrLen%2!=0):
#         newArr = [arr[((arrLen+1)//2)-1]]
#     elif(arrLen%2==0):
#         newArr = [ arr[(arrLen//2)-1], arr[((arrLen//2)+1)-1] ]
#         # newArr = [ arr[(arrLen//2)-1], arr[(arrLen//2)] ]
#     print(newArr)
# elif(arrLen<0):
#     print("Enter a poitive number")
    
# arr = []
# arrLen = int(input("how many elements have you got : "))
# for i in range(arrLen):
#     print("enter your elements name : ")
#     element = str(input())
#     arr.append(arrLen)
    
# print(arr)    
    
# arr = []
# arrLen = int(input("how many elements have you got : "))
# for i in range(arrLen):
#     print("enter your elements name : ")
#     element = str(input())
#     arr.append(arrLen)
#     print(arr)
    
#     if(arrLen%2!=0):
#       newArr = [arr[((arrLen+1)//2)-1]]
#     elif(arrLen%2==0):
#         newArr = [ arr[(arrLen//2)-1], arr[((arrLen//2)+1)-1] ]
#         # newArr = [ arr[(arrLen//2)-1], arr[(arrLen//2)] ]
#     print(newArr)
# #     print(newArr)

arr = []
arrLen = int(input("how many elements have you got : "))
if arrLen>=0:
    print(type(arrLen))
    for i in range(arrLen):
        print("enter your element name:")
        element = str(input())
        arr.append(arrLen)
        
print(arr)
        
if(arrLen%2!=0):
    newArr =[arr[((arrLen+1)//2)-1]]
elif(arrLen%2==0):
    newArr = [arr[(arrLen//2)-1], arr[(((arrLen//2)+1)-1)]]
    print(newArr)

if arrLen<0:
    print("enter a positive number")
    


# arr = []
# arrLen = int(input("how many elements you have got:"))
# if(arrLen>=0):
#     print(type(arrLen))
#     for i in range(arrLen):
#         print("enter your elements name:")
#         element = str(input())
#         arr.append(element)
#     print(arr)
#     newArr = [arr[0],arr[3]]
#     print(newArr)
