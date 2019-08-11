    l=input().split()
    for j in range(1,n,2):
        l[j],l[j-1]=l[j-1],l[j]
    for x in l:
        print(x,end=" ")
    print()
