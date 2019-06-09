#Problem : https://www.hackerearth.com/challenges/competitive/barclays-india-hackathon-2019-round-2-indicidual-challenge/algorithm/maxmul-f6d1d3d9/

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    print (a[n-1]*a[n-2] if a[n-1]*a[n-2] > a[0]*a[1] else a[0]*a[1])
