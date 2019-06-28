from bisect import bisect_left

ip = []
n = int(input())
for i in range(n):
	ip.append(int(input()))
#ip = list(map(int, input().split()))

op = 0		#total no of operation(s)
stack = []
res = []
flag = 0

for i in ip:
	if len(res)>0 :
		mid = len(res)//2
		k = bisect_left(res, i)	#find pos of cuurent element i.e. (greatest value smaller than ip[i] ) + 1  #log(n)
		
		#choosing preferable side
		if k > mid+1:
			flag = 1
		else:
			flage = 0		

		#inserting new element		
		if flag:
			for k in range(n+1):
				stack.append(res.pop())
				op += 1
			res.append(i)
			op += 1
			for k in range(n+1):
			 	res.append(stack.pop())
		else:
			for _ in range(k):
			 	stack.append(res.pop(0))
			res.insert(0,i)
			for _ in range(k):
			 	res.insert(0,stack.pop())
		if not k:
			op += 1
		else:
			op += ((2 * k) + 1) if k <= mid else (2 * (len(res) - k) - 1)
	else:
		res.append(i)
		op += 1
print(op)							#-------------------------------------------
