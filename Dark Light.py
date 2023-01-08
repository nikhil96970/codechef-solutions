for _ in range(int(input())):
    n, k = map(int, input().split())
    if (k == 0):
        if (n % 4 != 0):
            print("ON")
        else:
            print("OFF")
    else:
        if (n % 4 != 0):
            print("AMBIGUOUS")
        else:
            print("ON")
