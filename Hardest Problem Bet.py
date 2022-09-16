# cook your dish here
n = int(input())
for i in range(n):
    (a,b,c) = map(int,input().split(" "))
    if (c==min(a,b,c)):
        print("Alice")
    elif(b==min(a,b,c)):
        print("Bob")
    else:
        print("Draw")
