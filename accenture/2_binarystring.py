def binarystring(str):
    a=int(str[0])
    i=1
    while i< len(str):
        if str[i]=='A':
            a &= int(str[i+1])
        elif str[i]=='B':
            a |= int(str[i+1] ) 
        else:
            a ^=int(str[i+1])
        i+=2
    return a
 
print(binarystring('1C0C1C1A0B1'))              
