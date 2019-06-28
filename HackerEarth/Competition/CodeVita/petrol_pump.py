import math

ip = list(map(int, input().split()))

s = math.ceil(sum(ip) / 2)

first = []
sec = []

for i  in reversed(ip):
	if i < s:
		first.append(i)
		s -= i
	else:
		sec.append(i)

print(sum(first) if sum(first) > sum(sec) else sum(sec))
