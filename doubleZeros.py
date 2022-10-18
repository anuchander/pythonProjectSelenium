
'''
/*Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array *in place*, do not return anything from your function.
input: [1,0,2,3,0,4,5,0]
output: null
After calling the function input array is now [1,0,0,2,3,0,0,4]
'''

def doublezero(a):
    i=0
    while(i<len(a)-1):
        if a[i]==0:
            a.insert(i+1, 0)
            del a[len(a)-1]
            i+=2
        else:
            i+=1






    print(a)



a=[1,0,2,3,0,4,5,0]
print("The given array is: ", a)
doublezero(a)
