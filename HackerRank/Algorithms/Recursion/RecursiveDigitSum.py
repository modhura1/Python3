#https://www.hackerrank.com/challenges/recursive-digit-sum/problem


def recur (a):
    if a//10 == 0:
        print (a)
        exit(0)
    tot = 0
    while (a!=0):
        tot += a%10
        a //= 10
    recur(tot)


n, k = map(int, input().split())
p = 0
while (n!=0):
    p += n%10
    n //= 10
recur(p*k)


#9 out of 11 test cases passed
