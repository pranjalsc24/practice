def palindrome(a,b):
    for i in range(a, b+1):
        reverse = 0
        temp = i
        while temp != 0:
            remainder = temp % 10
            reverse = (reverse * 10)+ remainder
            temp = temp // 10
            if i == reverse:
                print(reverse, end=" ")


palindrome(100,200)

