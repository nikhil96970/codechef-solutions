for i in range(int(input())):
    n,m=map(int,input().split())
    if m>=n:
        print(n)
    else:
        t=n+(n-m)
        print(t)
