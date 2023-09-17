# n = int(input("Enter the value of n: ")) # taking input from user
# sum = 0
# for i in range(1, n+1):
#     sum += i          #sum=sum+i
# print("The sum of first", n, "numbers is:", sum)


# using recursion

def sums(n):
    if n==0:
        return 0
    else:
        return n+sums(n-1)
    
n=int(input("enter number"))
print(sums(n))