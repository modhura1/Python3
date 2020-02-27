#https://www.hackerrank.com/challenges/tutorial-intro/problem

#!/bin/python3

v = int(input())
n = int(input())
arr = list(map(int, input().rstrip().split()))
#print(arr)

for i in range(n):
    if arr[i]==v:
        print(i)
