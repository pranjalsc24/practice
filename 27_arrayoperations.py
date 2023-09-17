# SUM OF ELEMENTS FOR SQUARE MATRIX:
def add(arr):
    res=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            res=res+arr[i][j]
    return res

# arr=[[1,2,3],[4,5,6],[3,4,5]]
# ans=add(arr)
# print(ans)

list=[]
n=int(input("enter degree of matrix: "))
list1 = []
for i in range(n):
    list2 =[]
    print(f'the elements in the {i}th row')
    for j in range(n):
        a=int(input())
        list2.append(a)
    list1.append(list2)
print(list1) 
print("sum of elements:")
    
print(add(list1))




# Sum of individual rows:
def indirows(arr):
   
    for i in range(len(arr)):
        res=0
        for j in range(len(arr)):
            res=res+arr[i][j]
        print(f'for individual row: ',res)   
            
arr=[[1,2,3],[4,5,6],[3,4,5]]
ans=indirows(arr)




# Sum of individual columns:
def indirows(arr):
   
    for i in range(len(arr)):
        res=0
        for j in range(len(arr)):
            res=res+arr[j][i]
        print(f'for individual column: ',res)   
            
arr=[[1,2,3],[4,5,6],[3,4,5]]
ans=indirows(arr)
print(ans)



# Sum of diagonal elements:
def diagonal(arr):
    res=0
    for i in range(len(arr)):
       
        for j in range(len(arr)):
            if i==j:
                res=res+arr[i][j]
    return res
            
arr=[[1,2,3],[4,5,6],[3,4,5]]
ans=diagonal(arr)
print(ans)







