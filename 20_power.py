def power(x,n):
    if n==0:
        return 1
    else:
        return x**power(x,n-1)
    
x=int(input("enter base:"))
n=int(input("enter power: "))  
print(power(x,n)) 