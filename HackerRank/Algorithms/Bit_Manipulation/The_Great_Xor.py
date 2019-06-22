#Problem : https://www.hackerrank.com/challenges/the-great-xor/problem

def check(x):
    count = 0
    for i in range(1,x):
        if i^x > x:
            count += 1
    return count    
    
    
for _ in range(int(input())):
    x = int(input())
    res = check(x)
    print(res)
    
    
# 63.63% solved
