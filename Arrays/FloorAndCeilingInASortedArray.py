# URL : http://www.geeksforgeeks.org/search-floor-and-ceil-in-a-sorted-array/
inp = [1, 2, 8, 10, 10, 12, 19]
x = 7.99


def myBisect_left(inp, x, lo=0, high=len(inp)):
    if lo >= high:
        return None
    elif lo == high - 1:
        if x <= inp[lo]:
            return lo
        else:
            return lo + 1
    else:
        mid = lo + (high - lo - 1) / 2
        if x <= inp[mid]:
            return myBisect_left(inp, x, lo, mid + 1)
        else:
            return myBisect_left(inp, x, mid + 1, high)

    

def getFloor(inp, x):
    if x < inp[0]:
        return None
    elif inp[0] == x:
        return 0
    else:
        ind = myBisect_left(inp, x)
        if ind == len(inp):
            return inp[-1]
        elif inp[ind] == x:
            return x
        else:
            return inp[ind - 1]

if __name__ == '__main__':
    for x in range(21):
        print x, getFloor(inp, x)
