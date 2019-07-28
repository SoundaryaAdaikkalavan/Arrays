    n=int(input())
    a=list(map(int,input().split()))
    e=0
    for i in range(0,n):
        for j in range(i+1,n):
            c=a[i]^a[j]
            d=bin(c)[2:]
            e=e+d.count("1")
    print(2*e)
