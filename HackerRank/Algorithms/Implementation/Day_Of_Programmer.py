#https://www.hackerrank.com/challenges/day-of-the-programmer/problem

#!/bin/python3

D = "26.09.1918"
LD = "12.09"
NLD = "13.09"
i = int(input())
#print(i)

if i==1918:
    print(D)
elif i%100==00:
    if i > 1918:
        print(LD + '.' + str(i) if (i/100)%4==0 else NLD + '.' + str(i))
    else:
        print(NLD + '.' + str(i) if (i/100)%4==0 else LD + '.' + str(i))
elif (i%4==0):
    print(LD + '.' + str(i))
else:
    print(NLD + '.' + str(i))
