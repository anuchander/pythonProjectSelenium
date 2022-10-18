'''
 Given an array of integers, return the indices of the two numbers whose sum is equal to a given target.
 * Given nums = [2, 7, 11, 15], target = 9.
The output should be [0, 1].
Because nums[0] + nums[1] = 2 + 7 = 9.
'''

def twosum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if target-nums[i]==nums[j]:
                return i, j




nums=[2,11,15,7]
target=9
x,y = twosum(nums, target)
print("The indices are: ", x, y)
