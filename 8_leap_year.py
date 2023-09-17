n=int(input("Enter yeaar: "))

if ((n%400==0) or (n%100!=0 and n%4==0)):
    print("leap year")

else:
    print("not leap year")    
