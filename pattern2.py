# 5 5 5 5 5 ----------------- easy
# 5 5 5 5 
# 5 5 5 
# 5 5 
# 5

# def pattern3(n):
   
#     for i in range(n,0,-1):
       
#         for j in range(1,i+1):
#             print(n,end=' ')
#         # print("\r")
#         print(' ')
             

# a=int(input("Enter the number of lines:")) 
# pattern3(a) 



# 1 1 1 1 1         
# 2 2 2 2 
# 3 3 3 
# 4 4 
# 5



# def pattern3(n):
#     a=0
#     for i in range(n,0,-1):
#         a+=1
#         for j in range(1,i+1):
#             print(a,end=' ')
#         # print("\r")
#         print(' ')
# a=int(input("Enter the number of lines:")) 
# pattern3(a) 


# 1 
# 3 3 
# 5 5 5 
# 7 7 7 7 
# 9 9 9 9 9

def pattern3(n):
    a=0
    for i in range(1,n+1):
        a+=1
        for j in range(1,i+1):
            print((a*2-1),end=' ')
        # print("\r")
        print(' ')
a=int(input("Enter the number of lines:")) 
pattern3(a) 

