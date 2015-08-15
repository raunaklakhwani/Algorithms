inp = [100, 80, 60, 70, 60, 75, 85]
s = []

def calculateSpan(inp):
    '''
    The idea is to basically get the oreceding index from the current element
    which I have called in my function as hi.
    Then I need to do only i - hi to get the span.
    To get the hi(i.e preceding closest index to the current element), I have used stack approach
    Refer to URL : http://www.geeksforgeeks.org/the-stock-span-problem/ for more info
    '''
    span = []
    if len(inp) > 0 :
        s = []
        s.append(0)
        span.append(1)
        
        for i in xrange(1,len(inp)):
            stock = inp[i]
            while len(s) > 0 and stock >= inp[s[-1]]:
                s.pop()
                
            hi = s[-1] if len(s) > 0 else -1
            span.append(i-hi)
            s.append(i)
    return span


if __name__ == '__main__':
    print calculateSpan(inp)