# 1 2 3 4 5 
# 2 2 3 4 5 
# 3 3 3 4 5 
# 4 4 4 4 5 
# 5 5 5 5 5

# rows = 5
# for i in range(1, rows + 1):
#     for j in range(1, rows + 1):
#         if j <= i:
#             print(i, end=' ')
#         else:
#             print(j, end=' ')
#     print()


# 1  
# 2  4  
# 3  6  9  
# 4  8  12  16  
# 5  10  15  20  25  
# 6  12  18  24  30  36  
# 7  14  21  28  35  42  49  
# 8  16  24  32  40  48  56  64  

rows = 8
# rows = int(input("Enter the number of rows "))
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        # multiplication current column and row
        # square = i * j
        print(i * j, end='  ')
    print()