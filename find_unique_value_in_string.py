#16. Write a program string =aaabbc Find unique values

def find_unique_char(str1):
    n=len(str1)
    i=0
    result=''
    while(i<n):
        c=str1[i]
        count=0
        while(i<n and str1[i]==c):
            count+=1
            i+=1
        result+=str1[i-1]
        result+=str(count)
        print(result)
    for j in range(len(result)):
        if result[j] == '1':
            print("The unique character is:", result[j-1])
            return result[j-1]

str1 = 'aaabbc'
print("The given string is: ", str1)
unique_char=find_unique_char(str1)
print("The unique character is :", unique_char)