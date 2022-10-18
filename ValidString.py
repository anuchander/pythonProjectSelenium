import math
import os
import random
import re
import sys


#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
    # Write your code here
    strdict = {}
    for a in s:
        if a not in strdict:
            strdict[a] = 1
        else:
            strdict[a] = strdict[a] + 1
    print(strdict)
    count = 0
    dict_value = list(strdict.values())[0]
    print(dict_value)
    for value in strdict.values():
        if value == dict_value:
            continue
        elif value == dict_value + 1 or value == dict_value - 1:
            count += 1
    print("The count of values more/less is;", count)
    if count <= 1:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':
#    fptr = open(os.environ['/Users/anu/PycharmProjects/PythonSelenium/output.txt'], 'w')

    s = input()

    result = isValid(s)
    print(result)

 #   fptr.write(result + '\n')

  #  fptr.close()
