# x = input("Enter : ")
# match x:
#      case '1':
#         print('Hello to you too!')
#      case '2':
#          print('See you later')
#      case other:
#          print('No match found')

# mainBalance = 1600
# i=0
# while i<10:
    
#     def deposite(mainBalance):
#         amount  = int(input("enter an amount (TAKA): "))
#         previousBalance = mainBalance
#         mainBalance = mainBalance + amount
#         print("Deposit amount         : ", amount)
#         print("Your Prervious Balance : ", previousBalance)
#         print("Your  Current Balance  : ", mainBalance)
#         newBalance = mainBalance
#         return newBalance
        
    

    
#     def withdraw(mainBalance):
#         amount = int(input("enter an amount (TAKA): "))
#         previousBalance = mainBalance
#         if(amount<mainBalance):
#              mainBalance = mainBalance - amount
#         print("withdrawn amount         : ", amount)
#         print("Your Prervious Balance : ", previousBalance)
#         print("Your  Current Balance  : ", mainBalance)
#         newBalance = mainBalance
#         return newBalance
    
#     def initialPage():
#         print("""
#                 .-----------------------------------------------.
#                 |              MAYER DOWYA ATM                  |
#                 | 1. check balance                              |
#                 | 2. deposite                                   |
#                 | 3. withdraw                                   |
#                 |_______________________________________________|
                
#                 """)
        
#         selectedOption = input("choose your option(example: 2):")
#         match selectedOption:
#             case '1':
#                 print("your balance is: ",mainBalance, "TAKA")
#             case '2':
#                 # amount  = int(input("enter an amount (TAKA): "))
#                 deposite(mainBalance)
                
                
#             case '3':
#                 # amount  = int(input("enter an amount (TAKA): "))
#                 withdraw(mainBalance)
#             case other:
#                 print("Please enter correct number.")
#         newBalance = deposite(mainBalance)
#         # return newBalance
                
#     mainBalance =  newBalance
#     initialPage()  
    
   
    # mainBalance = newBalance
    
    
mainBalance = 1600
# i=0
# while i<10:
    

def deposit(mainBalance):
        amount  = int(input("enter an amount (TAKA): "))
        previousBalance = mainBalance
        mainBalance = mainBalance + amount
        print("Deposit amount         : ", amount)
        print("Your Prervious Balance : ", previousBalance)
        print("Your  Current Balance  : ", mainBalance)
        newBalance = mainBalance
        return newBalance
        
    

    
def withdraw(mainBalance):
        amount = int(input("enter an amount (TAKA): "))
        previousBalance = mainBalance
        if(amount<mainBalance):
             mainBalance = mainBalance - amount
        print("withdrawn amount         : ", amount)
        print("Your Prervious Balance : ", previousBalance)
        print("Your  Current Balance  : ", mainBalance)
        newBalance = mainBalance
        return newBalance
    
def initialPage():
        print("""
                .-----------------------------------------------.
                |              MAYER DOWYA ATM                  |
                | 1. check balance                              |
                | 2. deposit                                    |
                | 3. withdraw                                   |
                |_______________________________________________|
                
                """)
        
        selectedOption = input("choose your option(example: 2):")
        match selectedOption:
            case '1':
                print("your balance is: ",mainBalance, "TAKA")
            case '2':
                # amount  = int(input("enter an amount (TAKA): "))
                deposit(mainBalance)
                newBalance = mainBalance
                
            case '3':
                # amount  = int(input("enter an amount (TAKA): "))
                withdraw(mainBalance)
                newBalance = mainBalance
            case other:
                print("Please enter correct number.")
        newBalance = deposit(mainBalance)
        return newBalance
                
# mainBalance =  newBalance
initialPage()  