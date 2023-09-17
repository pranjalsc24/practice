# what is gcd:
# gcd greatest common divisor for ed (20,40)  in this among the all factors 
#   of 0 and 40 20 is greatst commom factot 





def gcd(a,b):
    res=[]
    if(a>b):
        m=a
    else:
        m=b
    for i in range(1,m):
        if(a%i==0 and b%i==0):
            g=i 
            
               
    print(f"GCD: {g} ")

    lcm=a*b/g

    print(f"LCM:{lcm}")


print(gcd(36897,241234))