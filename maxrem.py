n=int(input())
s = list(map(int, input().split()))
s = list(set(s))
s.sort()
print(s)
if len(s)==1:
	print(0)
else:
	print(s[-2]%s[-1])
