#Problem : https://www.hackerrank.com/challenges/sum-vs-xor/problem

n = int(input())
print(1 << (n.bit_length() - bin(n).count('1')))

'''
Explanation :

Totally a mathematical trick.
just count total numbers of ZERO present in binary number of given n, 
and answer will be the 2 to the power of (total num of zero).

It is simply concept of the Hamming weight of a number. 
In a lower-level language, One probably uses a nifty SIMD within a register trick or a library function to compute this. 
In Python, the shortest and most efficient way is to just turn it into a binary string and count the '1's: bin(n).count('1')

You can get the number of zeros by subtracting ones(num) from the total number of digits : n.bit_length() - bin(n).count('1'))
'''
