def fibonacci(n):
    a=1
    b=1
    print(f"{a}, {b}, ",end="")

    for i in range(1,n-1):
        c=a+b
        print(f"{c}, ",end='')
        a=b
        b=c

n= int(input("Enter a number: "))
fibonacci(n)


# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """

#         if n==0:
#             return 0
#         elif n==1:
#             return 1
#         else:
#             return self.fib(n-1)+self.fib(n-2)


class Solution:
    #Function to return list containing first n fibonacci numbers.
    def printFibb(self,n):
        # your code here
        first = 0
        second = 1
        third = 1
        lis = []
        for i in range(n):
            lis.append(third)
            third = first + second
            first = second
            second = third
        return lis




