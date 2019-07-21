#code
import math
for i in range (int(input())):
    n,m=input().split()
    n=int(n)
    m=int(m)
    print(math.factorial(n+m)//(math.factorial(n)*math.factorial(m)))
