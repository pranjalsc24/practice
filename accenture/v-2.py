def FindCount(n):
    if n is None:
        return 0
    digit_count= [0]*10

    for digit in n:
        digit=int(digit)
        digit_count[digit]+=1

    for i in range(len(n)):
        if digit_count[i]!=int(n[i]):
            return 0

    digit_count=sum(1 for count in digit_count if count>0)
    return digit_count        


number=input("Enter number: ")
print(FindCount(number))
print(FindCount("12340"))