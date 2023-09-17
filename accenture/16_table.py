def table(n):
    res=[]
    for i in range(1,11):
        # print(f"{n}*{i}=",n*i)
        res.append(n*i)
    print(res)    
    return sum(res)

print(table(5))    
