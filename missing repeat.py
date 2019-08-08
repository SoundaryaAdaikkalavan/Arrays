t=int(input())

for test in range(t):
    n=int(input())
    count=[0]*(n+1)
    temp=input().split()
    
    
    for i in range(n):
            count[int(temp[i])]+=1
    
    repeat=int(0)
    miss=int(0)
    for i in range(1,n+1):
        if(count[i]>1):
            repeat=i
        elif(count[i]<1):
            miss=i
        
            
    print(repeat,end=" ")
    print(miss)
