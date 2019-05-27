#problem : https://www.hackerrank.com/challenges/3d-surface-area/problem

def surfaceArea(A,H,W):
    area = 2*H*W
    for j in range(W):  area += A[0][j]
    for j in range(W):  area += A[H-1][j]
    for i in range(H):  area += A[i][0]
    for i in range(H):  area += A[i][W-1]
    for i in range(H-1):
        for j in range(W):  area += abs(A[i][j]-A[i+1][j])
    for i in range(H):
        for j in range(W-1):    area += abs(A[i][j]-A[i][j+1])
    return area
    
if __name__ == '__main__':
    HW = list(map(int, input().split()))
    A = []
    for _ in range(HW[0]):
        A.append(list(map(int, input().rstrip().split())))
    result = surfaceArea(A,HW[0],HW[1])
    print(result)
