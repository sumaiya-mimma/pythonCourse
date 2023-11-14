                # x = input("Enter : ")
                # match x:
                #      case '1':
                #         print('Hello to you too!')
                #      case '2':
                #          print('See you later')
                #      case other:
                #          print('No match found')



# userDB = [
#     ['111', 1111, 1000],
#     ['222', 2222, 2000],
#     ['333', 3333, 3000],
#     ['444', 4444, 4000],
#     ['555', 5555, 5000],
# ]

userDB = [1,2,3,4,5,6]
userCardNumber = int(input("Enter card your card Number : "))

flag = 0
for i in range(len(userDB)):
    if((userDB[i])==userCardNumber):
        print("yes")
        flag = 1
        break  
if(flag==0):
    print("No")
        


# mainBalance = 1600

# userPass = "1234"

# def deposite(mainBalance):
#     amount  = int(input("enter an amount (TAKA): "))
#     inputPass = input("enter your PIN : ")
#     if(inputPass == userPass):
#         previousBalance = mainBalance
#         mainBalance = mainBalance + amount
#         print("Deposit amount         : ", amount)
#         print("Your Prervious Balance : ", previousBalance)
#         print("Your  Current Balance  : ", mainBalance)
#         return mainBalance
#     else:
#         print("Wrong PIN! Please try again.")
#         return mainBalance
    



# def withdraw(mainBalance):
#     amount = int(input("enter an amount (TAKA) : "))
#     inputPass = input("enter your PIN : ")
#     if(inputPass == userPass):
#         previousBalance = mainBalance
#         if(amount<mainBalance):
#             mainBalance = mainBalance - amount
#             print("withdrawn amount         : ", amount)
#             print("Your Prervious Balance : ", previousBalance)
#             print("Your  Current Balance  : ", mainBalance)
#             return mainBalance
#         else:
#             print("You don't have enough Balance!")
#             return mainBalance
        
              

# i=0
# while i<1:
#     # userCardNumber = input("Enter your card number : ")
#     print("""
#             .-----------------------------------------------.
#             |              MAYER DOWYA ATM                  |
#             | 1. check balance                              |
#             | 2. deposite                                   |
#             | 3. withdraw                                   |
#             | 4. Reset Password                             |
#             |_______________________________________________|
            
#             """)
    
    # selectedOption = input("choose an option : ")
    # match selectedOption:
    #     case '1':
    #         inputPass = input("enter your PIN : ")
    #         if(inputPass == userPass):
    #             print("your balance is : ",mainBalance, "TAKA")
    #         else:
    #             print("Wrong PIN! Please try again")
    #     case '2':
    #         # amount  = int(input("enter an amount (TAKA): "))
    #         mainBalance = deposite(mainBalance)
    #     case '3':
    #         # amount  = int(input("enter an amount (TAKA): "))
    #         mainBalance =  withdraw(mainBalance)
    #     case '4':
    #         inputPass = input("enter your current PIN : ")
    #         if(inputPass==userPass):
    #             newPass = input("enter a new PIN : ")
    #             if(len(newPass) == 4):
    #                 userPass = newPass
    #             else:
    #                 print("Enter 4 digits PIN number.")
                
    #     case other:
    #         print("Please enter correct number.")




