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
""""
#I M TAKING ARRAY INPUT
arr=list(map(int,input().split()))

#NOW LET'S CHECK LENGTH OF NUM(OUR ARRAY)

n= len(arr)

#lets apply insertion sort logic
# WE HAVE VERY SMALL ARRAY SO IT is BEST TO USE 

for i in range(1, n):
    temp = arr[i]        # element to place
    j = i - 1

    while j >= 0 and arr[j] > temp:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = temp


print(arr)

#yes now its working!
"""
"""""
# Node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None
arr = [1, 2, 3, 4, 5]


for value in arr:
    new_node = Node(value)

    if head is None:
        head = new_node
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = new_node

if head is None:
    print(-1)
elif head.next is None:
    head = None
else:
    temp = head
    while temp.next.next:
        temp = temp.next
    temp.next = None


if head is None:
    print(-1)
else:
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next

"""

#Find the missing number in an array





#Problem Statement: Given an integer N and an array of size N-1 containing N-1 numbers between 1 to N. Find the number(between 1 to N), that is not present in the given array..
"""""
Examples
Example 1:
Input Format: N = 5, array[] = {1,2,4,5}
Result: 3
Explanation: In the given array, number 3 is missing. So, 3 is the answer.
"""
""""
n=int(input()) #taking user input in int
arr=list(map(int,input().split())) #took array input

expected_sum = n*(n+1)//2  #sum of natural numbers formula 
actual_Sum = sum(arr)

missing_number= expected_sum-actual_Sum
print(missing_number)
"""
""""
Find the Largest element in an array



26

Problem Statement: Given an array, we have to find the largest element in the array.

Examples
Example 1:
Input:
 arr[] = {2, 5, 1, 3, 0}  
Output:
 5  
Explanation:
  
5 is the largest element in the array.
 
"""
arr= list(map(int,input().split())) #took array input
largest=arr[0]  #asssumed that first number is largest

for num in arr:    #checking using for looop
    if num > largest:  
         # ex: if arr[1]>arr[0] then arr[1] will be largest 
        largest=num
print(largest)