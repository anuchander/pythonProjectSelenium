
'''
  Write a program String= aaabbc, output =a3b2c1


Write pgm for the string contains number,alphabet and special char.
Give the count of spl char.and execute them.
String a=aaaabbbbbccc. WAP to find 2nd most repeated character in the string.

'''

#Run String lenght encoding and decoding
def str_encoding(str1):
    n = len(str1)
    i=0
    result=''
    while(i<n):
        c= str1[i]
        count=0
        while(i<n and str1[i]==c):
            count+=1
            i+=1
        result+=(str1[i-1])
        result+=(str(count))
    return result


str1 = 'aaabbc'
print("The given string is:", str1)
return_val=str_encoding(str1)
print(return_val)