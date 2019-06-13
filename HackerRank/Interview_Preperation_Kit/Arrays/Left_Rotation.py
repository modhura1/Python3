#Problem : https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

N,d = map(int, input().split())
a = list(map(int, input().split()))
new = []
for i in range(N):
    new.append(a[(d+i)%N])
print(*new, sep = " ")
