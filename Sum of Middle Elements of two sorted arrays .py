#Given 2 sorted arrays A and B of size N each. Print sum of middle elements of the array obtained after merging the given arrays.
#Solution
def merge(a,b,n):
    c=[]
    l=0
    k=0
    while l<n and k<n:
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
        while k<n:
            c.append(b[k])
            k+=1
    print(c[n-1]+c[n])
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(y) for y in input().split()]
    b=[int(y) for y in input().split()]
    merge(a,b,n)
            
        
            
