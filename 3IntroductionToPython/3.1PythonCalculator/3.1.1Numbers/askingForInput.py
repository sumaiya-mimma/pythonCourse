arr = []
arrLen = int(input("how many elements are your in your array/list : "))
i = 0
while i<arrLen:
    print("enter element no", i+1, ":")
    element = int(input())
    arr.append(element)
    i = i+1
    
print(arr)
