n = int(input())
all = list(map(int, input().strip().split()))
fst = list(map(int, input().strip().split()))
snd = list(map(int, input().strip().split()))
trd = list(map(int, input().strip().split()))
t1 = sorted(all)
t2 = sorted(fst)
for i in range(len(fst)+1):
    if i == len(fst):
        print(t1[i])
    else:
        if t1[i] == t2[i]:
            continue
        else:
            print(t1[i])
            break

t1 = sorted(snd)
for i in range(len(snd)+1):
    if i == len(snd):
        print(t2[i])
    else:
        if t1[i] == t2[i]:
            continue
        else:
            print(t2[i])
            break

t2 = sorted(trd)
for i in range(len(trd)+1):
    if i == len(trd):
        print(t1[i])
    else:
        if t1[i] == t2[i]:
            continue
        else:
            print(t1[i])
            break


#passed 15/15 test cases.
