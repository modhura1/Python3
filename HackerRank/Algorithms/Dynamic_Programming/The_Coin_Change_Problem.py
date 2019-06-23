#Problem : https://www.hackerrank.com/challenges/coin-change/problem

n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [1]+[0]*n
for i in c:
    if i > n:                     #if coin > value, there's no reason to use it
        continue
    dp[i] += 1                    #coin by itself as a set
    for j in range(i+1, n+1):     #fill the remaining sets with a new possibility with this coin 
        dp[j] += dp[j-i]
print(dp[-1])
