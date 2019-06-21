#Problem : https://www.hackerrank.com/challenges/maximum-element/problem

st = [0]

for _ in range(int(input())):
    N = list(map(int, input().split()))
    if (N[0] == 1):
        st.append(max(N[1], st[-1]))
    elif (N[0] == 2):
        st.pop(-1)
    elif (N[0] == 3):
        print (st[-1])    
