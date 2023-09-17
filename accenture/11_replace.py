def replacechr(str,ch1,ch2):

    if len(str)==0:
        print("null")

    if ch1 and ch2 not in str:
        return str
    
    if ch1==ch2:
        return str

    res=''
    for i in str:
        if i==ch1:
            res+=ch2
        elif i==ch2:
            res+=ch1
        else:
            res+=i

    return res

print(replacechr('apples','o','o'))                