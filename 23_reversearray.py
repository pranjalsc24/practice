def reverse(arr):
    n=len(arr)
    i=0
    j=n-1
    while i<j:
        temp=arr[i]
        arr[i]=arr[j]
        arr[j]=temp
        i+=1
        j-=1

    return arr

arr = [10, 324, 45, 90, 9808] 
Ans = reverse(arr)
print(Ans)    