#problem : https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/practice-problems/algorithm/pair-sums/

n,k = [int(x) for x in input().split()]
a = list(map(int, input().split()))
a.sort()
h = [None] * (2 * n)
flag = 0


def hash_func(key):
    hash_key = k-key
    h[hash_key] = key


if k<a[0] and k>2*a[n-1]:
    print("NO")
else:
    for i in range(n):
        hash_func(a[i])
    for i in range(n):
        if h[i]!=None:
            if h[h[i]-1]==h[i]:
                print("YES")
                flag = 1

print("NO" if flag==0 else "")

#partially_accepted(60%)
