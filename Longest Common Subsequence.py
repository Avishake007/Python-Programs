#Given two sequences, find the length of longest subsequence present in both of them. Both the strings are of uppercase.
#Solution
def lcs(s1,s2,i,j,dp):
    if i>=len(s1) or j>=len(s2):
        return 0
    elif s1[i]==s2[j]:
        return 1+ lcs(s1,s2,i+1,j+1,dp)
    if dp[i][j]!=-1:
        return dp[i][j]
    else:
        l=lcs(s1,s2,i+1,j,dp)
        r=lcs(s1,s2,i,j+1,dp)
        dp[i][j]=max(l,r)
        return dp[i][j]
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    s1=input()
    s2=input()
    dp=[[-1 for i in range(n)] for j in range(m)]
    print(lcs(s1,s2,0,0,dp))


    
