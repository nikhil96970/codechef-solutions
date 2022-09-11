t=int(input())
for i in range(t):
    cnt=0
    a,b,c,d=map(int,input().strip().split())
    if(a==c or a==d):
        cnt+=1
    if(b==c or b==d):
        cnt+=1 
    if(cnt==0):
        print(2)
    elif(cnt==2):
        print(0)
    else:
        print(1)
