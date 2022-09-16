t= int(input())
for i in range(t):
    s=input()
    t=input()
    a=""
    for x in range(5):
        if s[x] == t[x]:
            a+="G"
        else:
            a+="B"
    print(a)
