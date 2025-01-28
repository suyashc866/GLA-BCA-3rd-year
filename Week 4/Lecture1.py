# ======================================================

#                      LECTURE : 1

# ======================================================


# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,1]

# Output: 1

# Example 2:

# Input: nums = [4,1,2,1,2]

# Output: 4

# Example 3:

# Input: nums = [1]

# Output: 1

# ==========================================================
# def singleNumber(nums):
#     result = 0
#     for num in nums:
#         result ^= num  # XOR all numbers
#     return result

# ans = singleNumber([1,2,2,3,1])
# print(ans)
# ==========================================================