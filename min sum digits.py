#code
t=int(input())
for i in range (t):
    n=int(input())
    a=input().split()
    a.sort()
    x=n//2
    even=[]
    odd=[]
    for i in range (n):
        if(i%2==0):
            even.append(a[i])
        else:
            odd.append(a[i])
    num1=''.join(even)
    num2=''.join(odd)
    print(int(num1)+int(num2))
    
    
