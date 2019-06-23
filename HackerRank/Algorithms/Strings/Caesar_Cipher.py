#Problem : https://www.hackerrank.com/challenges/caesar-cipher-1/problem?h_r=internal-search

n = int(input())
s = input()
k = int(input())
s_modi = ''
for i in range(len(s)):
    diff = 0
    if 97 <= ord(s[i]) <= 122:     #if small letter
        asc = ord(s[i]) + k 
        if asc <= 122:
            s_modi += chr(asc)
        else:
            diff = asc - 123
            asc = (97 + (diff % 26)) if diff >= 26 else 97 + (asc - 123) 
            s_modi += chr(asc)

    elif 65 <= ord(s[i]) <= 90 :     #if Capital letter
        asc = ord(s[i]) + k 
        if asc <= 90:
            s_modi += chr(asc)
        else:
            diff = asc - 91
            asc = (65 + (diff % 26)) if diff >= 26 else 65 + (asc - 91)
            s_modi += chr(asc)
    else:
        s_modi += s[i]

print(s_modi)
