# n=int(input("size of the matrix: "))
# m=int(input("Enter number of rows: "))
# n=int(input("Enter number of coloumns: "))
# res=[]
# for i in range(0,m):
#     for j in range(0,n):
#         a=int(input())
#         res.append(a)

# # e=len(res)
# res.sort()
# print(res)
# u=print(res[::2])  
# v=print(res[1::2])  
# r=u[1]+v[1]
# print(r)

n=int(input("enter the size of array:"))
res=[]
even=[]
odd=[]
for i in range(n):
    a=int(input())
    res.append(a)
    if i%2==0:
        even.append(a)
    else:
        odd.append(a) 



#    sorting
even.sort()
odd.sort()
print("even: ",even)
print("odd: ",odd)

add=print("addition:",even[-2]+odd[-2])

# res.sort()
# print(res)
# print("even:",res[::2])
# print("odd:",res[1::2] )

  

        
