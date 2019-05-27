#Problem : https://www.hackerrank.com/challenges/bon-appetit/problem

#!/bin/python3
nk = list(map(int, input().rstrip().split()))
bill = list(map(int, input().rstrip().split()))
b = int(input())
s = sum(bill, -bill[nk[1]])/2
if(b==s):
    print('Bon Appetit')
else:
    print(int(b-s))
