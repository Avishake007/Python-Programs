#Given a positive integer N, find the Nth fibonacci number. Since the answer can be very large, print the answer modulo 1000000007.
#Solution
t=int(input())
for _ in range(t):
    n=int(input())
    dp=[-1 for i in range(n+1)]
    dp[0]=0
    dp[1]=1
    if n==1:
        print(1)
    else:
        for i in range(2,n+1):
            dp[i]=dp[i-1]%1000000007+dp[i-2]%1000000007
        print(dp[n]%1000000007)
