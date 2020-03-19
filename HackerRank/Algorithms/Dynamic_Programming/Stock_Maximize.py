#https://www.hackerrank.com/challenges/stockmax/problem

#!/bin/python3
t = int(input())
for i in range (t):
    n = int(input())
    prc = list(map(int, input().rstrip().split()))
    profit = 0
    pos = 0
    pos2 = 0
    while(pos2<n-1):
        max = 0
        for j in range (pos,n):
            if prc[j]>max:
                max = prc[j]
                pos2 = j
        #print('max = '+str(max)) 
        #print('pos = '+str(pos))
        #print('pos2 = '+str(pos2))
        buy = 0
        for k in range(pos, pos2):
            buy += prc[k]
        profit += prc[pos2]*(pos2-pos) - buy
        pos = pos2+1
    print(profit)
