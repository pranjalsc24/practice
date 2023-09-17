# n=int(input("Enter number: "))
# r=0
# while(n!=0):
#     d=n%10
#     r=r*10+d
#     n=n//10

# print(f"reverse: {r}")    


# using for
num = int(input("Enter a number: "))
reverse = 0
sum=0
for i in range(len(str(num))):
    remainder = num % 10
    reverse = (reverse * 10) + remainder
    sum=sum+remainder
    num = num // 10
print("The reverse of the number is:", reverse)
print("The sum of the number is:", sum) 
    
   


#using recursion:


