# 1. Check Palindrome
 
# Problem Preview
# Write a program to find if a given string S is a palindrome or not. If palindrome print "Palindrome" otherwise print "Not a palindrome".
# Input Format
# The first line contains a string S.
# Output Format
# Display a single line output showing the result.
# Sample Input
# racecar
# Sample Output
# Palindrome


s=input()
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

# TEST CASE :- 
# racecar
# massachusetts
# malayalam


# 2.Count Digits


# Take the following as input.
# A number
# A digit
# Write a function that returns the number of times digit is found in the number. Print the value returned.
# Input Format
# Integer (A number) Integer (A digit)
# Output Format
# Integer (count of times digit occurs in the number)
# Sample Input
# 5433231 
# 3
# Sample Output
# 3
# Explanation
# The digit can be from 0 to 9. Assume decimal numbers.In the given case digit 3 is occurring 3 times in the given number.


number = int(input()) 
digit = int(input())   
count = 0
while number > 0:
    last_digit = number % 10
    if last_digit == digit:
        count += 1
    number //= 10
print(count)




# Test Case 
# Input :- 1

# 1000000000 
# 0 
# Output :- 9

# Input :- 2
# 0
# 1
# Output :-  0

# Input :- 3
# 99999223
# 1
# Output :-  0


# Input :- 4
# 929121319
# 1
# Output :-3
