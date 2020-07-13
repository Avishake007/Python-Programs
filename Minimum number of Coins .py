'''
Given a value N, total sum you have. You have to make change for Rs. N, and there is infinite supply of each of the denominations in Indian currency, i.e., you have infinite supply of { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000} valued coins/notes,
Find the minimum number of coins and/or notes needed to make the change for Rs N.
'''
#Solution
n=int(input())
for _ in range(n):
    t=int(input())
    s=[1,2,5,10,20,50,100,200,500,2000]#storing the given values of coins/notes in array s
    s=s[::-1]
    a=[]# Creating a empty to store the answer
    for k in s:
        if t>=k:#if  t<k means t//k will return 0 which will not cause any change
            l=t//k
            a+=[k]
            t=t-l*k
        if t==0:#It means we have achieved whole of t's value and thus don't need further calculation
            break
    for j in a:
        print(j,'',end='')
    print()
