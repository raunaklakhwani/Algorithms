s = "123"


def permutations(fixed,dummy):
    if dummy == "":
        yield fixed
    else:
        i = 0
        while i < len(dummy):
            nfixed = fixed + dummy[i]
            cdummy =  dummy[:i] + dummy[i+1:]
            for perm in permutations(nfixed,cdummy):
                yield perm
            i += 1
        


def f():
    for i in range(10,20):
        yield i
        
for i in f():
    print i        
        
for m in permutations("",s) :
    print m   
#===============================================================================
# p = permutations(s, "")        
# while True:
#     print next(p)
#===============================================================================
