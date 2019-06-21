#Problem : https://www.hackerrank.com/challenges/flipping-bits/problem

base = 2**32 - 1
for _ in range(int(input())):
    print(int(input()) ^ base)
   
   
'''
Explanation : It can be done by either using the negation ~ operator, or by XORing the value with 2^32 -1 (all 1).
Complexity :  time - O(N)
              space - O(1)
'''
