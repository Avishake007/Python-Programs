'''
Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins. The order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, 
there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
'''
#Solution
def coin(arr,i,s,n,dp):
    if i<0 or i>=n or s<0:
        return 0
    if s==0:
        return 1
    if dp[i][s]!=-1:
        return dp[i][s]
    l=coin(arr,i,s-arr[i],n,dp)
    r=coin(arr,i+1,s,n,dp)
    if r==None:
        r=0
    if l==None:
        l=0
    dp[i][s]=l+r
    return dp[i][s]
t=int(input())
for i in range(t):
    n=int(input())
    a=[int(y) for y in input().split()]
    s=int(input())
    dp=[[-1 for i in range(s+1)]for j in range(n)]
    print(coin(a,0,s,n,dp))
