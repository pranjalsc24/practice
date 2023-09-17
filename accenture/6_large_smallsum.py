def LargeSmallSum(arr):
    list1=[]
    list2=[]
    for i in range(len(arr)):
        if i%2==0:
            list1.append(arr[i])
        else:
            list2.append(arr[i])
    list1.sort()
    list2.sort()        
    # print(list1)
    # print(list2)
    return list1[1]+list2[1] 

arr= [3 ,2, 1, 7, 5, 4]  
print(LargeSmallSum(arr))  



