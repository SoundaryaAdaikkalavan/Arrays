mp = dict()
    for i in a:
        if i in mp:
            mp[i] += 1
        else:
            mp[i] = 1
    flag = True
    for i in a:
        if mp[i] == 1:
            print(i)
            flag = False
            break
    if flag:
        print(0)
