T = int(input())
def input_data():
    global X
    X = int(input())
for i in range(0,T):
    if T >= 1 and T <= 60:
        input_data()
        if X >= 30:
            print("YES")
        else:
            print("NO")
