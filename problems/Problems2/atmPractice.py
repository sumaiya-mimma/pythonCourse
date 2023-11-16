def deposit(mainBalance):
    inputPin = int(input("enter your PIN:"))
    if inputPin == userDB[i][0]:
     userAmount = int(input("enter an amount(USD): "))
     previousBalance = mainBalance
     mainBalance = mainBalance + userAmount
     print("deposit amount : ", userAmount, "USD")
     print("your previous balance is: ", previousBalance, "USD")
     print("your current balance is :", mainBalance, "USD")

    else:
      print("your PIN is not valid")
    
def withdraw(mainBalance):
    inputPin = int(input("enter your PIN:"))
    if (inputPin == userDB[i][0]):
     userAmount = int(input("enter an amount(USD): "))
    previousBalance = mainBalance
    mainBalance = mainBalance - userAmount
    print("withdrawn amount : ", userAmount, "USD")
    print("your previous balance is: ", previousBalance, "USD")
    print("your current balance is :", mainBalance, "USD")









mainBalance = 10000

userDB = [
    ['1010','10.08', '1000'],
    ['2010','01.08', '2000'],
    ['3010', '30 AUGUST', '3000'],
]
userCardNumber= input("enter your card:")

flag = 0
for i in range(len(userDB)):
    if(userDB[i][0])==userCardNumber:
        # userPin = input("enter your pin number:")
        # if (userDB[i][1])==userPin:
            # mainBalance = userDB[i][2]
            flag = 1
            
            
        # print(mainBalance)
        # print(userPin)
        
       
    print("""
                        ___________________________
                        |       ISIS ATM          |
                        |                         |
                        |1. check balance         |
                        |2. deposit               |
                        |3. withdraw              |
                        |4. reset password        |
                        |_________________________|
         
                    """)

selectOption = input("choose an option: ")
match selectOption:
    case'1': 
        inputPin = (input("enter your Pin:"))
        if (inputPin==userDB[i]):
            print("your balance is: ", mainBalance, "USD")
        else:
            print("your PIN is not valid")
    case '2':
        mainBalance = deposit(mainBalance)
    case '3': 
        mainBalance = withdraw(mainBalance)
    case '4':
        inputPin = (input("enter your PIN:"))
        if inputPin == userDB[i][1]:
            userNewPin = (input("enter a new PIN:"))
            if (len(userNewPin) == 4):
                NewPin = userDB[i][1]
                print(NewPin)
            else:
                print("please enter 4 digit PIN")
        else:
            print("your PIN is not valid")