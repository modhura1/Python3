#Problem : https://www.hackerrank.com/challenges/sum-vs-xor/problem

count = 0
n = int(input())
if ( n == 0):
    count = 1
else:
    for i in range(n):
        if n + i == n ^ i:
            count += 1
        else:
            continue
print(count)

#80% solved
