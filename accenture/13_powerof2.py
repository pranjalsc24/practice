def countpower(i):
    count=0
    while i%2==0 and i!=0:
        count+=1
        i=i//2
    return count

def maxpower(a,b):
    maximum=0
    # number=a
    for i in range(a,b):
        temp=countpower(i)
        if temp>maximum:
            maximum=temp
            number=i
    return number


print(maxpower(1,20))


