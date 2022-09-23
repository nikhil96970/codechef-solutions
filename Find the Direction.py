# cook your dish here
for _ in range(int(input())):
    x=int(input())
    if(x%4==0):
        print('North')
    elif(x%4==1):
        print('East')
    elif(x%4==2):
        print('South')
    elif(x%4==3):
        print('West')
