# cook your dish here
for i in range(int(input())):
    shots = list(map(int, input().split()))
    team1 = 0
    team2 = 0
    for i in range(10):
        if i == 0 or i % 2 == 0:
            team1 += shots[i]
        else:
            team2 += shots[i]
    if team1 > team2:
        print(1)
    elif team2 > team1:
        print(2)
    else:
        print(0)
