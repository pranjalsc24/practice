import math

p=float(input("enter principle amount: "))
y=float(input("enter years: "))
r=float(input("enter intrest: "))

# p,y,r=input("enter your name and age: ").split(",")

s=(p*y*r)/100
c=p*pow((1+r/100),y)-p              #pow(x,y)

print(f"simple interest:{s} and compound interest:{c}")