# cook your dish here
n=int(input())
a=list(map(int,input().split(' ')))
ecount=0
ocount=0
for i in range (n):
    if(a[i]%2!=0):
        ocount+=1
    else:
        ecount+=1

if(ocount>=ecount):
    print("NOT READY")
else:
    print("READY FOR BATTLE")
