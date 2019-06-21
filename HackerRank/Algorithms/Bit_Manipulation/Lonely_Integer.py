#Problem : https://www.hackerrank.com/challenges/lonely-integer/problem

from collections import Counter 

n = int(input())
arr = list(map(int, input().split()))
if (n > 1):
    result = sorted(arr, key = arr.count)
    print(result[0])
else:
    print(arr[0])
