# https://pynative.com/print-pattern-python-examples/

# cnt=1
# while cnt<=5:
# print(cnt* '1')
# #cnt +=1


# 1
# 11   
# 111  
# 1111 
# 11111

# class Pattern(object):
#     def pattern1(self, a):

#         for i in range(0,a+1):
#             print("*"*i)
        

# a=int(input("enter no of line: "))
# p1=Pattern()
# p1.pattern1(a) 

# -----------------------------
# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("*",end=' ')
#         print("\r")    
# a=int(input("Enter the number of lines:")) 
# pattern(a)


# ---------------------pattern2------------------
# *****
# ****
# ***
# **
# *

# def pattern1(a):
#     for i in range(a,0,-1):
#         for j in range(1,i+1):
#              print("*",end=' ')
#         print("\r") 

# a=int(input("Enter the number of lines:")) 
# pattern1(a)


#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * * 
# 
# rows = 6
# for i in range(0, rows):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > i:
#             print(" ", end=' ')
#         else:
#             print("*", end=' ')
#             num += 1
#     print("")   

    # -----Alternative Solution:-----
# rows = 5
# for j in range(1, rows+1):
#     print("* " * j)    














# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

# def pattern2(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end=' ')
#         # print("\r")
#         print(' ')
             

# a=int(input("Enter the number of lines:")) 
# pattern2(a)   


# ----------reverse off first pattern--------------------
# def pattern2(n):
#     for i in range(n,0,-1):
#         for j in range(1,i+1):
#             print(j,end=' ')
#         # print("\r")
#         print(' ')
             

# a=int(input("Enter the number of lines:")) 
# pattern2(a)   


# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5

# def pattern3(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(i,end=' ')
#         # print("\r")
#         print(' ')
             

# a=int(input("Enter the number of lines:")) 
# pattern3(a) 

# 1 
# 2 1 
# 3 2 1 
# 4 3 2 1 
# 5 4 3 2 1

# def pattern3(n):
#     for i in range(0,n+1):
#         for j in range(i,0,-1):
#             print(j,end=' ')
#         # print("\r")
#         print(' ')

# a=int(input("Enter the number of lines:")) 
# pattern3(a) 


# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1
# def pattern3(n):
#     for i in range(n,0,-1):
#         for j in range(i,0,-1):
#             print(j,end='')
#         # print("\r")
#         print(' ')

# a=int(input("Enter the number of lines:")) 
# pattern3(a) 






