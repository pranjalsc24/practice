def DectoNBase( n,num):
    remainder=[]
    
    remainder.append(num%n)
    quotient=num//n
    
    while(quotient!=0):
        remainder.append(quotient%n)
        quotient=quotient//n

    remainder=remainder[::-1]
    print(remainder)
    res=''

    for i in remainder:
        if i>9:
            a=i-9
            a=64+a
            res+=chr(a)
        else:
            res+=str(i)   
    return res         
            


print(DectoNBase(12,718))     




