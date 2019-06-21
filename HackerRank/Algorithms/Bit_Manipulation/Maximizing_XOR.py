#Problem : https://www.hackerrank.com/challenges/maximizing-xor/problem

l = int(input())
r = int(input())
M = 0

for x in range(l,r+1):
    for y in range(l, r+1):
        M = max(M, x ^ y)
print(M)

'''
Complexity : time - O(N^2)
'''
