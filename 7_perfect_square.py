import math
# a=int(input("Enter a number: "))
# b=round(math.sqrt(a),2)

# if b*b==a:
#     print("perfect square")
# else:
#     print("not perfect square")


#  --------------using functions-------------
def perfect(n):
    c=round(math.sqrt(n),2)
    if c*c==n:
        print("perfect square")
    else:
        print("not perfect square")    

a=int(input("Enter a number: "))
ans=perfect(a)

