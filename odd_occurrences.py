#Given a sorted array A, size N, of integers; every element appears twice except for one. Find that element that appears once in array.
#Solution
def findodd(a):
    res=0
    for i in range(len(a)):
        res^=a[i]
    return res
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(y) for y in input().split()]
    print(findodd(a))
