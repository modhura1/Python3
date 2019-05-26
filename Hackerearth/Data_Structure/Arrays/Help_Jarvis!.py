#Problem : https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/help-jarvis-8a39566e/

def check_continuity(my_list):
    return all(a+1==b for a, b in zip(my_list, my_list[1:]))
    
n = int(input())
s = t = []
c=0
for i in range(n):  s.append(input())
for i in range(n):
    t = list(map(int, s[i]))
    t.sort()
    c=check_continuity(t)
    print("YES" if c==True else "NO")
