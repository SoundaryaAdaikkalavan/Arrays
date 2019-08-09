    print('('+str(x)+' '+str(y)+')',end=' ')
for i in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    x,y=0,0
    if sorted(arr,reverse = True) == arr:
        print('No Profit')
        continue
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            y=i-1
            if x !=y:
                pr(x,y)
            x=i
    pr(x,i)
    print()
