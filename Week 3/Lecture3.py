# ======================================================

#                      LECTURE : 3

# ======================================================
# Given an array , find the sum of all subarray sums.

# • Initialize n = length(A) (length of the array).
# • Initialize total_sum = 0 (to store the total sum of all subarray sums).
# • For i from 0 to n - 1:
# 	• Compute the contribution of A[i] to all subarray sums as: 
#         contribution=A[i]×(i+1)×(n−i)contribution 
# 	• Add contribution to total_sum.
# • End For.
# Return total_sum.

# ======================================================
# def sumOfAllSubarraySums(A):
#     n = len(A)
#     total_sum = 0
    
#     for i in range(n):
#         # Contribution of A[i] to the sum of all subarrays
#         total_sum += A[i] * (i + 1) * (n - i)
    
#     return total_sum

# # Example Usage
# A1 = [1, 2, 3]
# A2 = [5, 1, 3, 4]

# print(sumOfAllSubarraySums(A1))  # Output: 20
# print(sumOfAllSubarraySums(A2))   # Output: 60
# ======================================================