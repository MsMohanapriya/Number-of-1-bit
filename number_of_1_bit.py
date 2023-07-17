def Number_of_1_bit(number):
    count=0
    while(number>0):
        if number&1:
            count+=1
        number>>=1
    return count
            
    
    
    
number=int(input("enter the decimal number: "))
print(Number_of_1_bit(number))