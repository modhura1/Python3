n = int(input())
ip = []
t = []
diff = 0
for i in range(n):
    ip.append(int(input()))
t = sorted(ip, reverse = True)
                   
for i in range(len(ip)-1):
    for j in range(i+1,len(ip)):
        #t1 = ip.index(t[i])
        t1 = ip.index(t[i])
        t2 = len(ip)-1-ip[::-1].index(t[j])
        if t1<t2 and abs(t1-t2)>diff:
            diff = abs(t1-t2)
print(diff)


#Passed 7/15 test cases
