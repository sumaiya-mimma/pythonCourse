


print(r"c:\some\ages")
print(r"c:\some\name")
print(r"c:\some\text")

print(r'don\'t say \"No\"')

print("""usage:thingy[OPTIONS]
    -h   display this usage message
    -H   hostname hostname to connect to""")


# r to stop line break/missing letters 
# """ for multiple lines
# \ for putting two lines together
# "dont't" , if we want to wrap this string with single qoute than we can do this: 'dont\'t'. another ex. 
# "\"YES\"" this will print "YES"



print(3*('un'+'ium'+' '))
print(3*('un'+'ium')+' ')

letters = ['a','b','c','d','e','f','g']
letters.append('h')
letters.append('i')
letters.append('j')

print('before', letters)
# letters[2] = 'z'
# print('afteer', letters)
# print(letters[2])
print('from line 35',len(letters));

letters[2:5] = ['C','D','E']
print('after', letters);
letters[2:5] = [];
print('after removing ', letters);

print(len(letters));


userInput = int(input("Enter a year : "))
# print('yorn input : ', userInput ,type(userInput));

# if((userInput%400) == 0 and (userInput%4) == 0 ):
#     print('leap year')
# else:
#     print('this year is not laep year')


if((userInput%100)==0):
    if((userInput%400)==0):
        print(userInput, " is leap year");
    else:
        print(userInput, " is not leap year");
elif((userInput%4)==0):
    print(userInput, " is leap year");
else:
    print(userInput, ' is not leap year')
    
else:
    print(userInput, ' is not leap year')
    
    
    
    
    
    
    
    
    
    
    
    








