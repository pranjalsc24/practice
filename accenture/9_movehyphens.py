def MoveHyphen(str):
    str1=''
    str2=''
    for i in str:
        if i=='-':
            str1+=i

        else:
            str2+=i

    return str1+str2        

    # print(str1) 
    # print(str2)                  


print(MoveHyphen('Move-Hyphens-to-Front'))

