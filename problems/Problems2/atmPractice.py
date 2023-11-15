def deposit(mainBalance):
    userAmount = int(input("enter an amount(USD): "))
    mainBalnce = mainBalance + userAmount
    print("deposit amount : ", userAmount, "userAmount ")
    












mainBalance = 10000

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
        print("your balance is: ", mainBalance, "USD")
    case '2':
        mainBalance = deposit(mainBalance)
        
    # case '3':
    # case '4':