def linearsearch(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i]==x:
          
            return True
    return False
            

arr = [10, 324, 45, 90, 9808] 
Ans = linearsearch(arr,45)
print(Ans)        