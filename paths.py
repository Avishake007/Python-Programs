'''
The problem is to count all the possible paths from top left to bottom right of a MxN matrix with the constraints that from each cell you can either move to right or down.

Input:
The first line of input contains an integer T, denoting the number of test cases. The first line of each test case is M and N, M is number of rows and N is number of columns.

Output:
For each test case, print the number of paths.
'''
#Solution
def r(m,n,x,y):
    if x<0 or y<0 or x>=m or y>=n:
        return 0
    elif x==m-1 and y==n-1:
        return 1
    else:
        return r(m,n,x+1,y)+r(m,n,x,y+1)
t=int(input())
for t in range(t):
    m,n=list(map(int,input().split()))
    print(r(m,n,0,0))
    
