##Problem statement is in filename ite.txt

def base(bs):
	id = 0
	while (bs != 0):
		r = bs % 10	
		if id < r:
			id = r
		bs = bs // 10
	return id

def baseA(bs):
	id = 0
	for i in range(len(bs)):
		if id < ord(bs[i]):
			id = ord(bs[i])
	return id

def deci(a, p):
		decimal = 0
		l = len(a) - 1
		for i in range(l, -1, -1):	
			num = int(a[i])
			if(num >= 0):
				decimal = decimal + num * pow(p, (l - i))
		return decimal

def deciN(a, p, j):
		decimal = 0
		num = a
		if(num >= 0):
			decimal = decimal + num * pow(p, j)
		return decimal

def deciA(a, p):
		decimal = 0
		l = len(a) - 1
		for i in range(l, -1, -1):	
			num = ord(a[i])
			if(num >= 0):
				decimal = decimal + num * pow(p, (l - i))
		return list(map(int, str(decimal)))

ip = input()

flag = 0
if ip.isdigit():
	flag = 0
elif ip.isalpha():
	flag = 1

if flag:
	ans = []
	temp = []
	ansr = 0
	print(flag)
	new = sorted(ip)
	g = ord(new[-1]) - 54
	for i in range(len(ip)):
		bas = ord(ip[i])-55
		p = pow(g, ((len(ip)-1)-i))
		temp.append(bas * p)
	print(temp)
	ans.append(sum(temp))
	ansr = sum(ans)
	while True:
		b = base(ansr)
		if b == 9:
			print(ansr)
			break
		else:
			ansr = deci(list(map(int, str(ansr))), b+1)
			print(ansr)		
			s = str(ansr)
			m = map(int, s)
			asd = list(m)	
			le = len(asd)
			print(le)	
			if le == 1:
				print(ansr)
				break
else:
	ans = int(ip)
	while True:
		b = base(ans)
		if b == 9:
			print(ans)
			break
		else:
			ans = deci(list(map(int, str(ans))), b+1)
			s = str(ans)
			m = map(int, s)
			asd = list(m)	
			le = len(asd)	
			if le == 1:
				print(ans)
				break
