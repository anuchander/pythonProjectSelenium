'''
input in a file: 22MMXKmmWWWWA
sorted output: 22A1K1M2W4X1m2
'''
f = open ("/Users/anu/PycharmProjects/pythonProjectSelenium/rochetext.txt", "r")
s = f.readline()
print(s)

    #s = '22MMXKmmWWWWA'
ns =''
i=0
while(i<len(s)):
    c=s[i]
    count=1
    while(i<len(s) and s[i]==c):
        count+=1
        i+=1
        ns=ns+c
        ns=ns+str(count)
print(ns)


