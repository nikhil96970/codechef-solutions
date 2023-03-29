# cook your dish here
for _ in range(int(input())):
    p,m,l=map(int,input().split())
    d=m-(p-1)
    k=d*l
    print(k)
