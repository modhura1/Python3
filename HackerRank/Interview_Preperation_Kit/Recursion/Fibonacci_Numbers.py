#Problem : https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

def fibonacciShort(n):
    return (fibonacciShort(n-1) + fibonacciShort(n-2) if n > 1 else (0 if n == 0 else 1))

def fibonacci(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
print(fibonacciShort(n))
