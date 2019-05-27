#Problem : https://www.hackerrank.com/challenges/migratory-birds/problem

#!/bin/python3
arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
print(max(set(arr), key = arr.count))
