#Given two sorted arrays A and B of size M and N respectively and an element k. The task is to find the element that would be at the k’th position of the final sorted array.
#Solution
def merge(a,b,n,nn,m):
    c=[]
    l=0
    k=0
    while l<n and k<nn:
        if a[l]<b[k]:
            c.append(a[l])
            l+=1
        else:
            c.append(b[k])
            k+=1
    if l<n:
        while l<n:
            c.append(a[l])
            l+=1
    else:
        while k<nn:
            c.append(b[k])
            k+=1
    print(c[m-1])
t=int(input())
for i in range(t):
    n,nn,m=map(int,input().split())
    a=[int(y) for y in input().split()]
    b=[int(y) for y in input().split()]
    merge(a,b,n,nn,m)
            
        
            
