# def myFunction():
#     print("hello")

# myFunction()


 
# def area(a=2,b=3):
#     print(a*b)

# area()
 
# def area(b,a):
#     print(a*b)

# area(2,9)



# print()
# input()
# type()
# int()
# str()

# print("hello")


# def chechLeapYear(year):
#     if((year%100)==0):
#         if((year%400)==0):
#             print(year, "is a leap year")
#         else:
#             print(year, "is not a leap year")
#     elif((year%4)==0):
#         print(year, "is a leap year")
#     else:
#         print(year, "is not a leap year")
# def isOdd(number):
#     if((number%2)==0):
#         print(number, "is a even number")
#     elif((number%2)!=0):
#         print(number, "is an odd number")      
# userInput = int(input("Enter a year : "))
# chechLeapYear(userInput)
# isOdd(userInput)

# def checkLeapYear(year):
#     if((year%100)==0):
#         if((year%400)==0):
#             return (year),"is a leap year"
#            # print(year, "is a leap year")
#         else:
#             return (year),"is not a leap year"
#             # print(year, "is not a leap year")
#     elif((year%4)==0):
#         return (year),"is a leap year"
#         # print(year, "is a leap year")
#     else:
#         return (year),"is not a leap year"
#         # print(year, "is not a leap year")
    
# def isOdd(number):
#         if((number%2)==0):
#             return (number), "is an even number"
#             # print(number, "is an even number")
#         elif((number%2)!=0):
#             return (number), "is an odd number"
#             # print(number, "is an odd number")
    
# userInput = int(input("enter an year : "))
# checkLeapYear(userInput)
# isOdd(userInput)





# def simpleEquation(x):
#     return x**2+(x-1)

# print(simpleEquation(2)+2)

# def equation(x,y):
#     return (x*y)*5+(x-y)

# print(equation(5,3))
# def simpleEquation(x):
#     return "x**2+(x-1)", x**2+(x-1), x, "** 2 + (","-1 )"



def simpleEquation(x):
    return "(x**2+(x-1))", x**2+(x-1),  (x,'**2+(','-1)')



userValue = int(input("enter  number"))
print(simpleEquation(2)[0])
print(simpleEquation(userValue)[2],simpleEquation(userValue)[3],simpleEquation(userValue)[2],
simpleEquation(userValue)[4])
print(simpleEquation(userValue)[1])


# def equation(x):
#     return "x**2+(x-1)", 



















        
        
    

    









