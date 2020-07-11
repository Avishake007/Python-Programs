#Given a number N, check whether it is sparse or not. A number is said to be a sparse number if in the binary representation of the number no two or more consecutive bits are set.
#Solution
t=int(input())
for i in range(t):
    n=int(input())
    s=bin(n).replace('ob','')
    #print(s)
    f=0
    for i in range(len(s)-1):
        if s[i]==s[i+1] and s[i]=='1':
            f=1
            break
    if f==1:
        print(0)
    else:
        print(1)
