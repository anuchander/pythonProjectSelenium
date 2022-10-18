'''
/*Given an array of random numbers, Push all the zero’s of a given array to the end of the array.
 *  For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}, it should be changed
 *  to {0,0,0,0,1, 9, 8, 4, 2, 7, 6}.
 */
'''

a=[1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
print("The original given array is:", a)
read_index = len(a)-1
write_index = len(a)-1

while(read_index>=0):
    if a[read_index]!=0:
        a[write_index]=a[read_index]
        write_index -= 1
    read_index -= 1
while(write_index>=0):
    a[write_index]=0
    write_index-=1
print(a)


