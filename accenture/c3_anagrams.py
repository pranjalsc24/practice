def anagrams(str1,str2):
    str1 = str1.lower()
    str2 = str2.lower()
    # str1 = str1.replace(" ", "").lower()
    # str2 = str2.replace(" ", "").lower()
    print(str1)
    for char in str1:
        if char not in str2:
            return 'no'
        else:
            return 'yes'
        

print(anagrams("Listen","Silent"))        