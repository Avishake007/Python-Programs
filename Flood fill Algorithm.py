'''
Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.

Example:

{{1, 1, 1, 1, 1, 1, 1, 1},
{1, 1, 1, 1, 1, 1, 0, 0},
{1, 0, 0, 1, 1, 0, 1, 1},
{1, 2, 2, 2, 2, 0, 1, 0},
{1, 1, 1, 2, 2, 0, 1, 0},
{1, 1, 1, 2, 2, 2, 2, 0},
{1, 1, 1, 1, 1, 2, 1, 1},
{1, 1, 1, 1, 1, 2, 2, 1},
 };

 x=4, y=4, color=3 

{{1, 1, 1, 1, 1, 1, 1, 1},
{1, 1, 1, 1, 1, 1, 0, 0},
{1, 0, 0, 1, 1, 0, 1, 1}, 
{1, 3, 3, 3, 3, 0, 1, 0},
{1, 1, 1, 3, 3, 0, 1, 0},
{1, 1, 1, 3, 3, 3, 3, 0},
{1, 1, 1, 1, 1, 3, 1, 1},
{1, 1, 1, 1, 1, 3, 3, 1}, };
'''
#Solution
def change(arr,x,y,m,n,l,ll):
    if x<m and y<n and x>=0 and y>=0:
        if arr[x][y]==l:
            arr[x][y]=ll
        if y+1<n:
            if arr[x][y+1]==l:
                change(arr,x,y+1,m,n,l,ll)
        if x+1<m:
            if arr[x+1][y]==l:
                change(arr,x+1,y,m,n,l,ll)
        if x-1>=0:
            if arr[x-1][y]==l:
                change(arr,x-1,y,m,n,l,ll)
        if y-1>=0:
            if arr[x][y-1]==l:
                change(arr,x,y-1,m,n,l,ll)
        
            
t=int(input())
for _ in range(t):
    m,n=map(int,input().split())
    a=[int(y) for y in input().split()]
    arr=[[a[j] for j in range(i,i+n)] for i in range(0,n*m,n)]
    x,y,ll=map(int,input().split())
    
    change(arr,x,y,m,n,arr[x][y],ll)
    for i in range(m):
        for j in range(n):
            print(arr[i][j],'',end='')
    print()
