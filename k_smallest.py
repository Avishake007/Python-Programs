#Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. 
#It is given that all array elements are distinct.
#Solution:
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(y) for y in input().split()]
    m=int(input())
    a=sorted(a)
    print(a[m-1])
