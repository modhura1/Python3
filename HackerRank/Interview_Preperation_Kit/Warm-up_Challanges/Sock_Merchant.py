#problem : https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

dic = {}
n = int(input())
arr = list(map(int, input().split()))
c = 0
for i in range(n):
    try:
        dic[arr[i]] += 1
    except KeyError:
        dic[arr[i]] = 1
for i in dic:
    c += int(dic[i]/2)
print(c)
