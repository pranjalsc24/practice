import math


def triangle(a,b,c):
    if ((a+b>c) and (b+c>a) and (a+c>b)):
        print("triangle can be drawn...")

        if(a==b==c):
            print("equilateral")
        elif((a!=b) and (b!=c) and (c!=a)):
            print("scelene triangle")
        else:
            print("isosceles triangle")

    else:
        print("triangle cannot be drawn")


def Area(a,b,c):
    s=(a+b+c)/2
    A= math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"Area of triangle: {A}")


a=float(input("enter first side of triangle: "))
b=float(input("enter second side of triangle: "))
c=float(input("enter third side of triangle: "))

triangle(a,b,c)
Area(a,b,c)