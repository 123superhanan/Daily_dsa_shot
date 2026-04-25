
#array

from sympy import total_degree


nums = [1, 2, 3, 4, 5,5]
for num in nums:
    print(num)

#loop using index
# 
for i in range(len(nums)):
    print(i, nums[i])

#enumerate

for i,num in enumerate(nums):
    print(i, num)



#find mximum in array

max_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num
print("Maximum number:", max_num)

#count frequency of elements in array

fre ={}
for num in nums:
    if num in fre:
        fre[num] += 1
    else:
        fre[num] = 1
print("Frequency of elements:", fre)

#reverse an array two pointer approach
left = 0
right = len(nums)-1

while left < right:
    nums[left],nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
print("Reversed array:", nums)

#sliding window approach to find maximum sum of subarray of size k
k = 3
windoe_sum = sum(nums[:k])
print("Initial window sum:", windoe_sum)

#running sum
total = 0
for num in nums:
    total += num
print("Running sum:", total)


trget = 5
for i,num in enumerate(nums):
    if(num == trget):
        print("Target found at index:", i)
        

#duplicte elements in array
seen = set()
for num in nums:
    if num in seen:
        print(True)
        break
    seen.add(num)


#condition bsed move 
# rerrnge elements
# move all zeroes to end of array
#example: [0,1,0,3,12] -> [1,3,12,0,0]

nums_two = [0,1,0,3,12]
non_zero_index = 0
for i in range(len(nums_two)):
    if nums_two[i] != 0:
        nums_two[non_zero_index], nums_two[i] = nums_two[i], nums_two[non_zero_index]
        non_zero_index += 1
print("Array after moving zeroes:", nums_two)

#subarray problems
#find maximum sum of subarray of size k
#exp : [1,2,3,4,5], k=3 -> 12 (3+4+5)

k=3
max_sum = 0
for i in range(len(nums)-k+1):
    window_sum = 0
    for j in range(i, i+k):
        window_sum += nums[j]
    max_sum = max(max_sum, window_sum)
print("Maximum sum of subarray of size k:", max_sum)






#The dice problem

# def oppositeFaceOfDice(n):
#     if n == 1:
#         return 6
#     elif n == 2:
#         return 5
#     elif n == 3:
#         return 4
#     elif n == 4:
#         return 3
#     elif n == 5:
#         return 2
#     else:
#         return 1

# n = 2
# print(oppositeFaceOfDice(n))


# def secondSolution(n):
#     return 7-n

# n = 1
# print(secondSolution(n))

# #==========================
# # Given two integers n and m, find the closest integer to n that is divisible by m.
# #===========================
# def closest_number(n, m):
#     # find the quotient
#     closest = 0
#     min_difference = float('inf')

#     # Check numbers around n
#     for i in range(n - abs(m), n + abs(m) + 1):
#         if i % m == 0:
#             difference = abs(n - i)

#             if difference < min_difference or \
#             			(difference == min_difference and abs(i) > abs(closest)):
#                 closest = i
#                 min_difference = difference
#     return closest

  
# if __name__ == "__main__":
#   n = 13
#   m = 4
#   print(closest_number(n, m))