def armstrong(a):
    c1=c2=a

    count=0
    while (c1!=0):
        c1=c1//10
        count+=1

    # print(count)
    sum=0
    while(c2!=0):
        d=c2%10
        sum=sum+d**count
        c2=c2//10

    if (sum==a):
        print("Armstrong Nmuber")
    else:
        print("No Armstrong Nmuber")


a=int(input("enter a number:"))
armstrong(a)