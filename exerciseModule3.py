#16
# userInput = int(input("enter a number : "))
# if(userInput>17):
#     print((userInput-17)*2)
# elif(userInput<17):
#     print(userInput, "less than 17")
# else:
#     print("false")

 
    
    
#18




# userInput = int(input("how many numbers have you got  : "))
# for i in range(userInput):
#     print("enter number ", i+1, ":")
#     element = int(input())
#     i = i+1
# if("number 1" == "number 2" == "number 3"):
#     print(("number 1" + "number 2" + "number 3")*3)
 
 
 
    
#  #18   
    
# number1 = int(input("enter a number : "))
# print(number1)
# number2 = int(input("enter a number : "))
# print(number2)
# number3 = int(input("enter a number : "))
# print(number3)
# if(number1 == number2== number3):
#     print("values are equal")
#     print((number1 + number2 + number3)*3)
# elif(number1 != number2 != number3):
#     print("values are not equal")
# else:
#     print("not equal")


    
#14?
# date1 = (2014,7,11)
# date2 = (2014,7,2)
# days = date1 - date2
# print(days)
# from datetime import days
# date1 = (2014,7,11)
# date2 = (2014,7,2)
# delta = date1 - date2
# print(delta.days)



#10?
# n = 5
# print(n+n*n+n*n*n)




#13
# print("""a string that you \"don\'t\" \nthis \nis a........multi-line  \nheredoc string-----------> example""")





# #8
# myList = ["red","green","white","black"]
# newList = [myList[0], myList[3]]
# print(newList)







#7
# fileName= input("enter a file name : ")
# extension = fileName.split(".")[-1]
# print(extension)





#9
# exam_st_date = (11,12,2014)
# print("the examination will start from:" %exam_st_date)





#12
# import calendar
# print(calendar

# year = int(input("enter an year : "))
# print(year)
# def printyear(calender):





#22

# arr = []
# arrLen = int(input("how many numbers are in your list : "))
# for i in range(arrLen):
#     print("enter element number", i+1,":")
#     element=int(input())
#     arr.append(element)
#     i = i+1
# print(arr)
# if("arr", has element, "4"):
 
 
 
    

# 24
# userInput = (input("enter a letter:"))
# if(userInput == "a" or userInput == "e" or userInput == "i" or userInput == "o" or userInput == "u" or userInput == "A" or userInput == "E" or userInput == "I" or userInput == "O" or userInput == "U"):
#     print(userInput, "is a vowel")
# else:
#     print(userInput, "is not a vowel")




#15
# import math
# print(math.pi)

# r = 6
# volumeOfSphere = 4/3*3.14159*6*3
# print(volumeOfSphere)




#38
#

#37
# student = ("patrick", 23, "24th street,california")
# (name,age,address)=student
# print("name:", name)
# print("age:", age)
# print("age:", address)




#39
# pa = 10000
# int = 3.5
# yr = 7
# fv = ((pa)/((1+3.5)*7))
# print(fv)




#30
# base = 56
# height = 56
# area = ((base*height)/2)
# print(area)




# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# for x in range(numbers):
#     if(x==237):
#         print(x)
#         break
#     elif((x%2)==0):
#         print(x)






#33
# number1 = int(input("enter a number : "))
# print(number1)
# number2 = int(input("enter a number : "))
# print(number2)
# number3 = int(input("enter a number : "))
# print(number3)
# if(number1 == number2):
#     sum = ((number1+number2+number3)==0)
#     print(sum, "is 0")
# else:
#     print("not equal")





#34
# number1 = int(input("enter a number : "))
# print(number1)
# number2 = int(input("enter a number : "))
# print(number2)
# result = number1 + number2
# print(result)
# if(15<result<20):
#     print(20)
# else:
#     print("false")






#38?

# number1 = int(input("enter a number : "))
# print(number1)
# number2 = int(input("enter a number : "))
# print(number2)
# if(number1==number2):
#     print("true")
# elif((number1+number1)==5) or ((number1-number2)==5):
#     print("true")
# else:
#     print("false")




#40?


# x = ("x1","y1")
# y = ("x2","y2")
# (x3,y3
 
 
            
#28?

# numbers = [ 
#            386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527 
#     ]
# i = 0
# while i<=52:
#     print(numbers[i])
#     (numbers[i])-1
#     if((numbers[i]%2)==0):
#      print(numbers[i])



# 
arr = []
arrLen = int(input("how many elements you have got:"))
if(arrLen>=0):
    print(type(arrLen))
    for i in range(arrLen):
        print("enter your elements name:")
        element = str(input())
        arr.append(element)
    print(arr)
    if(arrLen%2!=0):
        newArr = [arr[((arrLen+1)//2)-1]]
    elif(arrLen%2==0):
        newArr = [ arr[(arrLen//2)-1], arr[((arrLen//2)+1)-1] ]
        # newArr = [ arr[(arrLen//2)-1], arr[(arrLen//2)] ]
    print(newArr)
elif(arrLen<0):
    print("Enter a poitive number")





















