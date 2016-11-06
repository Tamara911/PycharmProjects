def xo(s):
    s = s.upper()
    res1 = 0
    res2 = 0
    for i in s:
        if i == "O":
            res1 +=1
        if i == "X":
            res2 +=1
        else:
            pass
    if res1 == res2:
        return True
    else:
        return False

ff = xo("ddoffooxx")
print(ff)