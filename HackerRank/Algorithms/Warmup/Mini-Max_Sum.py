#Problem : https://www.hackerrank.com/challenges/mini-max-sum/problem


### APROACH 1 :

#!/bin/python3

def miniMaxSum(arr):
    arr.sort() 
    max = sum (arr, -arr[len(arr)-1]) 
    min = sum (arr, -arr[0]) 
    print (str(max)+" "+str(min))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
    
    
#Complexity : O(NlogN)


### APROACH 2 :

def miniMaxSum(arr):
    Min = min(arr)
    Max = max(arr)
    maxSum = sum (arr, -Min) 
    minSum = sum (arr, -Max) 
    print (str(minSum)+" "+str(maxSum))

arr = list(map(int, input().rstrip().split()))
miniMaxSum(arr)

#Complexity : O(N)
