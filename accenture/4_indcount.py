# abs() in Python. The Python abs() function 
# return the absolute value. The absolute value of any 
# number is always positive it removes the negative sign of a number 
# in Python.


def findcount(arr,n,num,diff):
    count=0
    res=[]
    for i in range(n):
        if (abs(arr[i]-num)<=diff) :
            count+=1
            res.append(i)
    print(res)        
    return  count   


arr=[12 ,3, 14, 56, 77, 13]
n=len(arr)
num=13
diff=2
print(findcount(arr,n,num,diff))