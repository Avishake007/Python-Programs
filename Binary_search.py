#Given a sorted array of integers and a key to be searched in the array. Print the position of the key in the array, if present. If it's not present in the array, report it. 
#Solution
def bin_search(A, left, right, k):
    p=0
    while left<=right:
        mid=(right+left)//2
        if A[mid]==k:
            p=1
            return mid
        elif A[mid]<k:
            left=mid+1
        else:
            right=mid-1
    if p==0:
        return -1
t=int(input())
for i in range(t):
n=int(input())
a=[int(y) for y in input().split()]
m=int(input())
print(bin_search(a,0,n-1,m))
