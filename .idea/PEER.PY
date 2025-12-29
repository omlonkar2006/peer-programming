""""
Count Maximum Consecutive One's in the array

Problem Statement: Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..

Examples
Example 1:
Input: prices = {1, 1, 0, 1, 1, 1}
Output: 3
Explanation: There are two consecutive 1’s and three consecutive 1’s in the array out of which maximum is 3.
"""

arr=list(map(int,input().split())) #took array input

max_count=0
current_count=0

for num in arr:
    if num==1:
        current_count +=1
        if current_count >max_count:
            max_count=current_count
    
else:
    current_count=0

print(max_count)

