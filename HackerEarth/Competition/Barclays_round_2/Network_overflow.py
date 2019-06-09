#Problem: https://www.hackerearth.com/challenges/competitive/barclays-india-hackathon-2019-round-2-indicidual-challenge/algorithm/network-overflow-96af2214/

n = int(input())
m = int(input())
available_packages = [0] * 200003
weight = []

for _ in range(m):
    weight.append(int(input()))

available_packages[0] = n
for i in range(m):
    p = available_packages[i]
    p = p - weight[i]
    if(p%2==0):
        r=int(p/2)
        s=r
    else:
        r=int(p/2) + 1
        s=r-1
    available_packages[2*i+1] = r
    available_packages[2*i+2] = s
sum = 0
for i in range(m,200003):
    if available_packages[i] > 0:
        sum += available_packages[i]
print(sum)


#Partially_solved
