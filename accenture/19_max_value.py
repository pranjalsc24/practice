def maximum(arr):
    for i in range(1,len(arr)):

        if arr[0]>=arr[i]:
            maximum=arr[0]
        else:
            maximum=arr[i]  

    return maximum,i


print(maximum([23 ,45, 82, 27 ,66 ,12 ,78, 13, 71, 86 ]))
          