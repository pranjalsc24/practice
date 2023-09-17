# def largest(arr):
#     max=arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] > max:
#             max = arr[i]
 
#     return max
 


# # a=largest([2,3,4,14,23,45])
# # print(a)

# arr = [10, 324, 45, 90, 9808] 
# Ans = largest(arr)
# print("Largest in given array is", Ans)

def largest(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max:
            max = arr[i]
 
    return max

arr = [10, 324, 45, 90, 9808] 
Ans = largest(arr)
print("Largest in the given array is", Ans)

