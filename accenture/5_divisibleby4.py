# def divisible(n,m):
#     list1=[]
#     list2=[]
#     sum1=0
#     for i in range(1,m+1):
#         if i%n==0:
#             list1.append(i)
#     # print(list1)
    
#     # print(sum(list1))
#     a=sum(list1)

#     for i in range(1,m+1):
#         if i%n!=0:
#             list2.append(i)
#     # print(list2)

#     b=sum(list2) 
    
#     return b-a
# n=4
# m=20
# print(divisible(n,m))




n = int(input())
m = int(input())
sum1 = 0
sum2 = 0
for i in range(1,m+1):
    if i % n == 0:
        sum1+=i
    else:
        sum2+=i
print(abs(sum2-sum1))



        
        
