# cook your dish here
#n=int(input())
for _ in range(int(input())):
    nb,bc,wt=map(int,input().split(' '))
    x=wt/bc
    if(x>=nb):
        print(int(nb))
    else:
        print(int(x))
