#string str1='hehllho'. After removing the duplicate characters we get 'helo'

str1='hehllho'
print("The given string is :", str1)

str2=''
for c in str1:
    if not c in str2:
        str2=str2+c
print("The non duplicate string is:", str2)

for i in range(len(str1)):
    c = str1[i]
    for j in range(i+1, len(str1)):
        if str1[j]==c:
            str1[j].replace(str1[j], "")



