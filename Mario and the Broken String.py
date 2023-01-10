for _ in range(int(input())):
    c=0
    l,m=[],[]
    k=int(input())
    s=input()
    for i in range(0,k//2):
        l.append(s[i])
    for i in range((k//2),k):
        m.append(s[i])
    if l==m:
        print("YES")
    else:
        print("NO")
            
