#Problem : https://www.hackerrank.com/challenges/xor-and-sum/problem

a = int(input(), 2)
b = int(input(), 2)

res = 0
for i in range(314160):
    res += a ^ (b << i)
print(res % 1000000007)
