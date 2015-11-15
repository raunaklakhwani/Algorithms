#URL : http://www.careercup.com/question?id=4830599367884800
def getTwoEqualSets(inp):
    inp.sort()
    start = 0
    end = len(inp) - 3
    s1,s2 = inp[-1],inp[-2]
    ls1,ls2 = 1,1
    s2Flag = False
    s1Flag = False
    while start <= end:
        if ls1 > ls2:
            if s1 > s2:
                s2 += inp[end]
                end -= 1
            else:
                s2 += inp[start]
                start += 1
            ls2 += 1
        elif ls1 < ls2:
            if s1 > s2:
                s1 += inp[start]
                start += 1
            else:
                s1 += inp[end]
                end -= 1
            ls1 += 1
        else:
            if s1 > s2:
                s2 += inp[end]
                end -= 1
                ls2 += 1
            else:
                s1 += inp[end]
                end -= 1
                ls1 += 1
    
    print s1,s2