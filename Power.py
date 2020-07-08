Problem: Given a number N, let the reverse of the number be R. The task is to print the output of the Expression pow(N,R), where pow function represents N raised to power R.
Time complexity: log(n)
Solution:
def power(x,y):
    if y==0:
        return 1
    temp=power(x,y//2)
    if y%2==0:
        temp=temp*temp
    else:
        if y>0:
            temp=x*temp*temp
        else:
            temp=(temp*temp)/x
    return temp
t=int(input())
for _ in range(t):
    n=int(input())
    nn=list(str(n))
    p=int(''.join(nn[::-1]))
    print(power(n,p))
