import math
def equation(a,b,c):
    d=b**2-(4*a*c)
    # e=math.sqrt((64))
    print(type(d))
    if (d>0):
        print("Real roots")
        x1=((-b)+math.sqrt(d))/2*a
        x2=((-b)-math.sqrt(d))/2*a
        print(f"Roots are:{x1} and {x2}")

    elif (d<0):
        print("complex roots")
        x3=-b/2*a  
        x4= math.sqrt(d)/2*a
        print(f"Roots are:{x3}+i{x4} and {x4}+i{x4}")

    else:
        print("equal roots")
        x5=(-b)/2*a
        print(f"Roots are:{x5} and {x5}")


print("Enter coefficients of equation:")
a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))

equation(a,b,c)




