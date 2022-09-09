t=int(input())
for i in range(t):
    c=0
    n=int(input())
    a=list(map(int,input().split()))
    for e in a:
        if(e>=10 and e<=60):
            c=c+1
    print(c)
            
