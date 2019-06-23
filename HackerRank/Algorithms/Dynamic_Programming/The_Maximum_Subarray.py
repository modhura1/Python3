#Problem : https://www.hackerrank.com/challenges/maxsubarray/problem

ip = []
for _ in range(int(input())):
    #n = 
    int(input())
    ip.append(list(map(int, input().split())))

for i in range(len(ip)):
    sumSubSeq = 0
    sumSubArr = 0
    for j in range(len(ip[i])):
        p = min(ip[i])
        q = max(ip[i])
        pos = ip[i].index(p) 
        if p > 0:                                  #if all elements are +ve
            sumSubSeq = sumSubArr = sum(ip[i])
        else:                                      #if atlest 1 element is -ve
            if q < 0:                              #if all elements are -ve
                sumSubArr = sumSubSeq = q
            elif pos == 0 or pos == len(ip[i])-1:  #if both +ve & -ve elements present and min element is present in terminal
                sumSubArr = sum(ip[i], -p)
                sumSubSeq = 0
                for k in range(len(ip[i])):
                    if ip[i][k] > 0:
                        sumSubSeq += ip[i][k]     
            else :                                  #if both +ve & -ve elements present and min element is Not present in terminal
                count = 0
                for k in range(len(ip[i])):
                    if ip[i][k] == p:
                        count += 1
                sumSubSeq = sum(ip[i], -(p * count))
                if count > 1:
                    count -= 1
                sumSubArr = sum(ip[i], -(p * count))
                
    print (str(sumSubArr) + " " + str(sumSubSeq))
    
    
# 80% solved
