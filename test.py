#THIS IS OUR QUE, 
"""
Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order.


The sorting must be done in-place, without making a copy of the original array.


Example 1

Input: nums = [1, 0, 2, 1, 0]

Output: [0, 0, 1, 1, 2]

Explanation:

The nums array in sorted order has 2 zeroes, 2 ones and 1 two

Example 2

Input: nums = [0, 0, 1, 1, 1]

Output: [0, 0, 1, 1, 1]

Explanation:

The nums array in sorted order has 2 zeroes, 3 ones and zero twos

Now your turn!

Input: nums = [1, 1, 2, 2, 1]
"""

#I M TAKING ARRAY INPUT
arr=list(map(int,input().split()))

#NOW LET'S CHECK LENGTH OF NUM(OUR ARRAY)

n= len(arr)

#lets apply insertion sort logic
# WE HAVE VERY SMALL ARRAY SO IT IT BEST TO USE 

for i in range(1, n):
    temp = arr[i]        # element to place
    j = i - 1

    while j >= 0 and arr[j] > temp:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = temp


print(arr)
