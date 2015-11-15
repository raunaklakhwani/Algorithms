#===============================================================================
# s = "ababa"
# d = "babab"
#===============================================================================

def get(s,d,index):
    if index == len(s) - 1:
        return (1,1,set(s[index]),set(d[index]))
    else:
        us,ud,uniques,uniqued = get(s,d,index + 1)
        if (s[index] in uniques and d[index] in uniqued) or (s[index] in uniqued and d[index] in uniques):
            return (us,ud,uniques,uniqued)
        elif (s[index] in uniques) or (s[index] in uniqued):
            if (s[index] in uniques):
                uniqued.add(d[index])
                return (us,ud + 1,uniques,uniqued)
            else:
                uniques.add(d[index])
                return (us + 1,ud,uniques,uniqued)
        elif (d[index] in uniques) or (d[index] in uniqued):
            if (d[index] in uniques):
                uniqued.add(s[index])
                return (us,ud + 1,uniques,uniqued)
            else:
                uniques.add(s[index])
                return (us + 1,ud,uniques,uniqued)
        else:
            uniqued.add(d[index])
            uniques.add(s[index])
            return (us + 1,ud + 1,uniques,uniqued)


#print get(s,d,0)

for _ in xrange(input()):
    N = input()
    s = raw_input()
    d = raw_input()
    res = get(s,d,0)
    print max(res[0],res[1])        
                
            