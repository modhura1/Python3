n, m = map(tuple, input().split())

from itertools import permutations 
  
# Get all permutations of [1, 2, 3] 
perm = permutations(list(n)) 

 
l = []
# Print the obtained permutations 
for i in list(perm): 
	if i > m:
		l.append(i)
if len(l) == 0:
	print (-1)
else:
	l.sort()
	print(int(''.join(l[0])))
