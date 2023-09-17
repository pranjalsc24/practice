def ProductSmallestPair(sum, arr):
    if len(arr)==0 or len(arr)<2:
        return -1
    arr.sort()
    for i in range(len(arr)):
        if arr[i]+arr[i+1]<=sum:
            return arr[i]*arr[i+1]
        else:
            return 0
        

Arr=[9 ,8, 3, -7, 3, 9  ]
sum=4
print(ProductSmallestPair(sum, Arr))      

