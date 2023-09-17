# num = int(input("Enter a number: "))
# reverse = 0
# c=num
# for i in range(len(str(num))):
#     remainder = num % 10
#     reverse = (reverse * 10) + remainder
#     num = num // 10

# if(c==reverse):
#     print("palindrome")   
# else:
#     print("not palindrome")    



# # for string:
# def palindrom(word):
#     return word==word[::-1]

# print(palindrom("madam"))  


# class Solution(object):
#     def isPalindrome(self, x):
       
#         if(x>=0):
#             c1=x
#             r=0
#             while(c1!=0):
#                 d=c1%10
#                 r = r*10+d
#                 c1=c1//10

#             return r==x
#         return False 

# a=int(input('Enter number: '))
# p1=Solution()
# print(p1.isPalindrome(a)) 


# for string :
def palindrome(s):
    
    n=len(s)
    i=0
    j=n-1

    while (i<n and j<n):
        if s[i] == s[j]:
            i+=1
            j-=1
        else:   
            return False
    return True        


print(palindrome("madam") )
print(palindrome("pranjal"))




    