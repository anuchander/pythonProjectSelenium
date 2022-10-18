
'''
input = "rotor"
input2 = "a"
input3 = "rater"
input4 = "tattarrattat"

'''
def palindrome(input):
    n = len(input)

    for i in range(0, n):
        print(i)
        for j in range(n-1,0,-1):
            print(i, j)
            if input[i]!=input[j]:
                return False
            else:
                i+=1


    return True

def pal2(input):
        string2 = input[::-1]
        if input == string2:
            return True
        else:
            return False

def pal3(input):
    for i in range(0, int(len(input) / 2)):
        if input[i] != input[len(input) - i - 1]:
            print(i, len(input)-i-1)
            return False
        else:
            return True

input = "rotor"
input3 = "rater"
input2 = "a"
input4 = "tattarrattat"
input5 = 'car'
#val = palindrome(input)
#val = pal2(input)
val=pal3(input5)
print(val)