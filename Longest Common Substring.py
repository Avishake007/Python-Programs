'''
Given two strings X and Y. The task is to find the length of the longest common substring.

Input:
First line of the input contains number of test cases T. Each test case consist of three lines, first of which contains 2 space separated integers N and M denoting the size of string X and Y strings respectively. The next two lines contains the string X and Y.

Output:
For each test case print the length of longest  common substring of the two strings .

Constraints:
1 <= T <= 200
1 <= N, M <= 100

Example:
Input:
2
6 6
ABCDGH
ACDGHR
3 2
ABC
AC

Output:
4
1
'''
#Solution
for _ in range(int(input())):
    n,m=map(int,input().split())
    arr1=list(input())
    arr2=list(input())
    mm=0
    dp=[[0 for i in range(n+1)] for j in range(m+1)]#creating a 2d array of shape(m+1,n+1)
    for i in range(1,m+1):
        for j in range(1,n+1):
            #print(arr2[i-1])
            if arr2[i-1]==arr1[j-1]:
                dp[i][j]=dp[i-1][j-1]+1# Adding 1 to dp[i-1][j-1] if arr2[i-1]==arr1[j-1]
                mm=max(mm,dp[i][j])# Stores the max in mm
            else:
                dp[i][j]=0
    print(mm)
                
