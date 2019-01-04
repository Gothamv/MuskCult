"""
 Given an array of positive and negative integers, find the first
 missing positive integer.
 For Example : [-2, -1, 0, 4, 6, 3] returns 1
"""


def find_missing(arr):
    max_ = max(arr)
    if max_ < 1:  # All negative values in the array
        return 1
    if len(arr) is 1:
        return 2 if arr[0] == 1 else 1
    list1 = [0] * max_  # Making a zero value list
    for i in range(len(arr)):
        if arr[i] > 0:
            if list1[arr[i] - 1] != 1:
                list1[arr[i] - 1] = 1  # Updating the list value to each time we find a +ve integer
    for i in range(len(list1)):
        if list1[i] == 0:
            return list1[i+1]
    return i+2  # if all the values are already filled


arr_ = [0, 2, 4, 5, -1, -4]
arr__ = [0, 1, 2, 3, 4, 5]
print(find_missing(arr_))
print(find_missing(arr__))
# added this line for second commit
