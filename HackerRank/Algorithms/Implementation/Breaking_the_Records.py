#Problem : https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

def breakingRecords(scores):
    H=L=h=l=0
    H=L=scores[0]
    for i in range(len(scores)):
        if (scores[i]>H):
            H=scores[i]
            h+=1
        elif (scores[i]<L):
            L=scores[i]
            l+=1
    return ([h,l])

n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breakingRecords(scores)
print(' '.join(map(str, result)))
