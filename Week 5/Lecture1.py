# ======================================================

#                      LECTURE : 1

# ======================================================



# FUNCTION count_bob_occurrences(A):
#     SET count = 0
#     SET n = length of A
    
#     FOR i from 0 to n - 3:
#         IF substring of A from index i to i+3 is "bob":
#             INCREMENT count
    
#     RETURN count







# FUNCTION count_amazing_substrings(S):
#     SET vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#     SET count = 0
#     SET n = length of S
    
#     FOR i from 0 to n - 1:
#         IF S[i] is in vowels:
#             count = count + (n - i)  # All substrings starting from index i
    
#     RETURN count % 10003



# FUNCTION transform_string(A):
#     SET vowels = {'a', 'e', 'i', 'o', 'u'}
#     SET result = EMPTY STRING
#     SET concatenated_string = A + A  # Step 1: Concatenate with itself
    
#     FOR each character c in concatenated_string:
#         IF c is uppercase:
#             CONTINUE  # Skip uppercase letters (Step 2)
#         ELSE IF c is in vowels:
#             APPEND '#' to result  # Replace vowels (Step 3)
#         ELSE:
#             APPEND c to result  # Keep other characters unchanged
    
#     RETURN result
