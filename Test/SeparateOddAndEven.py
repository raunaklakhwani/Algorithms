inp = [2,3,4,5,8,10,12,11]
inp = range(9)

def separateEAndO():
    print 'Hello'
    i = 0
    e = -1
    o = -1
    while i < len(inp):
        num = inp[i]
        #print num,
        if num & 1 == 1:
            print "Odd"
            if o == -1:
                o = i
        else:
            if e+1 != i and o >= 0:
                inp[e+1],inp[i] = inp[i],inp[e+1]
            e += 1
        i += 1
        print inp
    



if __name__ == '__main__':
    #print inp
    separateEAndO()
    #print inp