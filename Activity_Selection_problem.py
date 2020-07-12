'''
There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is start time of meeting i and F[i] is finish time of meeting i.

What is the maximum number of meetings that can be accommodated in the meeting room?
'''
#Solution

for _ in range(int(input())):
    n=int(input())
    a=[int(y) for y in input().split()]
    b=[int(y) for y in input().split()]
    c=[int(i+1) for i in range(n)]
    l=0
    for i in range(1,n):
        for j in range(n-i):
            if b[j]>b[j+1]:
                b[j],b[j+1]=b[j+1],b[j]
                a[j],a[j+1]=a[j+1],a[j]
                c[j],c[j+1]=c[j+1],c[j]
    p=1     
    s=b[0]
    d=str(c[0])
    for i in range(1,n):
        if a[i]>s:
            s=b[i]
            d+=' '+str(c[i])
            p+=1
   # print(p)
    print(d)
