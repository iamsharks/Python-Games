n,m=map(int,input().split())
arr=[]
for i in range(n):
    row=list(map(int,input().split()))
    arr.append(row)
for i in range(n):
    for j in range(n-i):
        print(*arr[i])