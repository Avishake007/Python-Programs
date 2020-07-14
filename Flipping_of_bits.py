'''
Given a non-negative number N and two values L and R. The problem is to toggle the bits in the range L to R in the binary representation of N, i.e, to
toggle bits from the rightmost Lth bit to the rightmost Rth bit. A toggle operation flips a bit 0 to 1 and a bit 1 to 0.
'''
#Solution
t=int(input())
for _ in range(t):
    m,l,r=map(int,input().split())
    m=list(bin(m).replace('0b',''))# Decimal to binary
    m=m[::-1]# Reversing the array
    for k in range(l-1,r):
        m[k]='1' if m[k]=='0' else '0'# toggling taking place
    s=''.join(m[::-1])
    print(int(s,2))#Binary to decimal
