#https://www.hackerrank.com/challenges/insertionsort1/problem?h_r=next-challenge&h_v=zen

n = int(input())
arr = list(map(int, input().rstrip().split()))
p = arr[-1]

if arr[0]>p:
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
        print(*arr, sep=' ')
    arr[0]=p
    print(*arr, sep=' ')
    exit(0) 
for i in range(n-2,-1,-1):
    #print(i)
    if arr[i]>p:
        arr[i+1]=arr[i]
        print(*arr, sep=' ')
    else:
        arr[i+1]=p
        print(*arr, sep=' ')
        exit()
