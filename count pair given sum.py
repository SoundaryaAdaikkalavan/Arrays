    t -= 1
    n,s = map(int, input().split())
    l = list(map(int, input().split()))
    perm = list(permutations(l,2))
    count = 0
    for i in perm:
        if sum(i) == s:
            count += 1
    print(int(count/2))
