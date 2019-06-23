#Problem : https://www.hackerrank.com/challenges/fibonacci-modified/problem

#!/bin/python3

import os

# Complete the fibonacciModified function below.
# Using Tabulation method
def fibonacciModified(t1, t2, n):
    f = [0] * (n+1)
    f[0] = t1
    f[1] = t2
    for i in range(2, n+1):
        f[i] = f[i-2] + (f[i-1])**2
    return f[n-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t1T2n = input().split()
    t1 = int(t1T2n[0])
    t2 = int(t1T2n[1])
    n = int(t1T2n[2])
    result = fibonacciModified(t1, t2, n)
    fptr.write(str(result) + '\n')
    fptr.close()    
