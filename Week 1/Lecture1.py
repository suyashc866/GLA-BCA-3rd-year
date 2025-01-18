#1.Print all factors/divisor of a given  +ve number.

# N = 10     factor = 1,2,5,10
# N =36      factor = 1,2,3,4,6,12,18,36
# range[1,N]
# =============

# N = int(input())

# i = 1
# while (i<=N):

# 	if(N%i ==0):       #”i is factor”
# 		print(i)

# 	i += 1
# =============

# 2.Read N,Print No of digits in N.

# N = 100  →3
# N = 5926 →5

# N / 10 =>5926 /10  →4 times divide => 4 digit


# =============
# N = int(input())

# digit = 0   # →Initialization

# while (N>0):  #→condition
# 	N = N//10 #→ Update (integer division)

# 	digit = digit + 1 #→ Work (preparing result)


# print(digit)
# =============

# Because N is loop control variable

# 3.Read N,Print sum of digits in N.
# N = 528 => sum = 15


# =============
# N = int(input())

# S = 0
# while(N>0):

# 	digit = N%10
# 	N = N // 10

# 	S += digit
# print(S)
# =============


# 4.Read N and a single digit ‘d ‘, add ‘d’ back to N
# N = 52
# d = 6
# Ans →526

# N * 10  →52 * 10 =>520
#        +d →520 + 6 =>526
# Ans = N * 10 + d

# Solution:

# N = int(input())
# d = int(input())
# print(N*10 +d)


# 5.Read N, Print reverse of N
# N = 123 → 321

# =============
N = int(input())

ans = 0
while (N > 0):    #or (N != -1)

	digit = N % 10
	N = N //10
	ans = ans * 10 + digit
print(ans) 
# =============