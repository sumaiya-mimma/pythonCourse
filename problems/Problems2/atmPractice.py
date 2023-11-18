def deposit(mainBalance):
    inputPin = int(input("enter your PIN:"))
    # flag = 0
    # for i in range(len(userDB)):
    if inputPin == userPin:
        #  flag = 1
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
    if inputPin == userPin:
     userAmount = int(input("enter an amount(USD): "))
     previousBalance = mainBalance
     mainBalance = mainBalance - userAmount
    # return mainBalance
     transactionFee = 0.5
     mainBalance = mainBalance - transactionFee
     print("withdrawn amount : ", userAmount, "USD")
     print("your previous balance is: ", previousBalance, "USD")
     print("your current balance is :", mainBalance, "USD")
     print("your transaction cost : " ,0.5, "USD")
# mainBalance = 10000
# userPin = 1234
userDB = [
     ['1010','1008', '1000'],
     ['2010','0108', '2000'],
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
             mainBalance = userDB[i][2]
             userPin = userDB[i][1]
             print(mainBalance)
             print(userPin)
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
        if (inputPin==userPin):
            print("your balance is: ", mainBalance, "USD")
        else:
            print("your PIN is not valid")
    case '2':
        mainBalance = deposit(mainBalance)
        
    case '3': 
        # inputPin = (input("enter your PIN:"))
        # if inputPin == userPin:
         mainBalance = withdraw(mainBalance)
    case '4':
        inputPin = (input("enter your PIN:"))
        if inputPin == userPin:
            userNewPin = (input("enter a new PIN:"))
            if (len(userNewPin) == 4):
                userPin = userNewPin 
                print(userPin)
            else:
                print("please enter 4 digit PIN")
        else:
            print("your PIN is not valid")
        
            
           
#         break
# if flag == 0:
#     print("errror")
    