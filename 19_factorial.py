#User function Template for python3
# class Solution:
#     def nCr(self, n, r):
#         # code here
        
#         def factorial(n):
#             fact=1
#             for i in range(1,n+1):
#                 fact=fact*i
#             return fact
        
#         if r>n:return 0    
#         res=(factorial(n)//(factorial(r)*factorial(n-r)))%(10**9+7)
        
#         return res
    
    # using recrion

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input("enter number"))
print(fact(n))
                
                