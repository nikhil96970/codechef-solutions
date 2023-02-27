# cook your dish here
for i in range(int(input())):
    n=int(input())
    arr1=list(map(int, input().split()))
    arr2=list(map(int, input().split()))
    t=0
    for i in range(n):
        if arr1[i]==arr2[i]:
            t+=1
    print(t)
