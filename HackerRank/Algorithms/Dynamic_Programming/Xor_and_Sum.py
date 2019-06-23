#Problem : 

a = int(input(), 2)
b = int(input(), 2)

res = 0
for i in range(314160):
    #b = b << i 
    #a = a ^ b
    res += a ^ (b << i)
print(res % 1000000007)
