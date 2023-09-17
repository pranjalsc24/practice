import math

# a=float(input("Enter radius: "))
# cx,cy=int(input("Enter x and y co-ordinate of center seprated by ',': ").split())
# px,py=int(input("Enter x and y co-ordinate of point seprated by ',': ").split())

# print(type(cx))


# a=float(input("Enter radius: "))
# # taking two input at a time
# cx, cy = [int(x) for x in input("Enter two values: ").split()]
# print("First Number is: ", cx)
# print("Second Number is: ", cy)



# d=float(math.sqrt((px-cx)**2 + (py-cy)**2))


import math

a=float(input("Enter radius: "))
cx,cy=input("Enter x and y co-ordinate of center seprated by ',': ").split()
px,py=input("Enter x and y co-ordinate of point seprated by ',': ").split()

# print(type(cx))

d=math.sqrt((float(px)-float(cx))**2+((float(py)-float(cy))**2))
print(f"distance: {d}")


if(d>a):
    print("point lies outside the circle...")

elif(d<a):
    print("point lies inside the circle...")
else:
     print("point lies on the circle...")




