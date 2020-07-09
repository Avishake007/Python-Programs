'''
You are given an integer N. You need to convert all zeroes of N to 5.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a single integer N denoting the number.

Output:
For each test case, there will be a new line containing an integer where all zero's are converted to 5.
'''
#Solution
def convertFive(n):
    # Code here
    n=list(str(n))
    k=['5' if l=='0' else l for l in n]
    return int(''.join(map(str,k)))
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        print (convertFive(int(input().strip())))
