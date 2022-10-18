import math
import os
import random
import re
import sys


#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    # print("Magazine value is:", magazine)
    # print("Note value is:", note)
    m_dict = {}
    n_dict = {}
    for a in magazine:
        if a not in m_dict:
            m_dict[a] = 1
        else:
            m_dict[a] += 1
    for a in note:
        if a not in n_dict:
            n_dict[a] = 1
        else:
            n_dict[a] += 1
    # print(m_dict)
    # print(n_dict)
    for k, v in n_dict.items():
        if k not in m_dict.keys():
            print('No')
            return
        elif v <= m_dict[k]:
            continue
        else:
            print('No')
            return
    print('Yes')

    for a in note:
        if a in magazine:
            continue
        else:
            print('No')
            break
        print('Yes')


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
