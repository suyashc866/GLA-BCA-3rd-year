# ======================================================

#                      LECTURE : 3

# ======================================================

# Longest Palindrome

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
# palindrome
#  that can be built with those letters.

# Letters are case sensitive, for example, "Aa" is not considered a palindrome.


from collections import Counter

def longest_palindrome(s: str) -> int:
    char_count = Counter(s)
    length = 0
    odd_found = False

    for count in char_count.values():
        if count % 2 == 0:
            length += count
        else:
            length += count - 1
            odd_found = True

    return length + 1 if odd_found else length

# Example Test Cases
print(longest_palindrome("abccccdd"))  # Output: 7
print(longest_palindrome("Aa"))        # Output: 1
