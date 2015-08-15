#URL : http://qa.geeksforgeeks.org/1666/google-interview-question-minimum-no-of-swaps
inp = [3,5,6,4,1,2]
d={1:3,2:6,4:5,3:1,6:2,5:4}


def getMinimumSwaps(start,end,inp):
    if start >= end:
        return 0
    else:
        if d[inp[end]] == inp[end-1]:
            return getMinimumSwaps(start,end-2,inp)
        else:
            #fix last
            partnerLast = d[inp[end]]
            index = inp.index(partnerLast)
            inp[end-1],inp[index] = inp[index],inp[end-1]
            last = 1 + getMinimumSwaps(start,end-2,inp)
            inp[end-1],inp[index] = inp[index],inp[end-1]
            
            #fix second last
            partnerSecondLast = d[inp[end-1]]
            index = inp.index(partnerSecondLast)
            inp[end],inp[index] = inp[index],inp[end]
            partnerSecondLast = 1 + getMinimumSwaps(start,end-2,inp)
            inp[end],inp[index] = inp[index],inp[end]
            
            return min(last,partnerSecondLast)

print getMinimumSwaps(0, len(inp) - 1, inp)