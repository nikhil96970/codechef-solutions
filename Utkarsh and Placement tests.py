# cook your dish here
for i in range(int(input())):
    companies=list(map(str,input().split()))
    offers=list(map(str,input().split()))
    for j in range(len(companies)):
        if companies[j] in offers:
            print (companies[j])
            break
    
