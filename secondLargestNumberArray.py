#int a[] = {3,67,45,11,2,52,98,70,14,32};

a =[3,67,45,11,2,52,98,70,14,32]

for i in range(len(a)):
    print(a[i], end=" ")
print()
for i in range(len(a)-1, -1, -1):
    print(a[i], end=" ")
print()
max=a[0]
second_max=a[1]
for i in range (len(a)):
    if a[i]>max:
        second_max=max
        max=a[i]
    elif a[i]>second_max:
        second_max=a[i]
print("The max element in the array is: ", max)
print("The second max element in the array is: ", second_max)




