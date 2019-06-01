#problem : https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

n = int(input())
a = list(input())
count = prev = 0
depth = (1 if a[0]=='U' else -1)
for i in range(1,n):
    if depth < 0 :
        prev = -1
    elif depth > 0:
        prev = 1
    if a[i] == 'U':
        depth += 1
    else:
        depth -= 1
    if depth == 0 and prev == -1 :
        count += 1
print (count)
