inp = [5, 1, 4, 3, 0, 2]
inp = [1,2,3]
inp = [1,2,3,5]
inp = [8,7]
inp = range(14,16)
bits = 31
def getTwoSets(inp, bit):
    zero = []
    one = []
    for i in inp:
        if (i >> bit) & 1:
            one.append(i)
        else:
            zero.append(i)
            
    return (zero, one)




m = 0
def recurse(one, zero, bit):
    if len(one) and len(zero):
        if len(one) == 1 and len(zero) == 1:
            return one[0] ^ zero[0]
        else:
            a = b = float("-inf")
            onezero, oneone = getTwoSets(one, bit)
            zerozero, zeroone = getTwoSets(zero, bit)
            
            if len(oneone) and len(zerozero):
                a = recurse(oneone, zerozero, bit - 1)
            
            if len(onezero) and len(zeroone):
                b = recurse(onezero, zeroone, bit - 1)
                
            m = max(a, b)
            
            if m == float("-inf"):
                m = recurse(one, zero, bit - 1)
                return m
            else:
                return m
    elif len(one):
        onezero,oneone = getTwoSets(one, bit)
        return recurse(oneone, onezero, bit - 1)
    elif len(zero):
        zerozero,zeroone = getTwoSets(zero, bit)
        return recurse(zeroone, zerozero, bit - 1)
    else:
        return 0  
    
    
zero, one = getTwoSets(inp, bits)
print recurse(one, zero, bits - 1)  
