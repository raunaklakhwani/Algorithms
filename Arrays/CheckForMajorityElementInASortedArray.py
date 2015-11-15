# URL : http://www.geeksforgeeks.org/check-for-majority-element-in-a-sorted-array/
from bisect import bisect_left, bisect_right
inp = [1, 2, 3, 3, 3, 10]
x = 3



def checkMaximumElementUtil(inp, x, start, end):
    mid = start + (end - start) / 2
    if inp[mid] == x:
        a = bisect_left(inp, x, start, mid)
        b = bisect_right(inp, x, mid + 1, end)
        # print a,b
        if (b - a) > (len(inp) >> 1):
            return True
        else:
            return False
    else:
        return False
        

def checkMaximumElement(inp, x):
    return checkMaximumElementUtil(inp, x, 0, len(inp) - 1)


if __name__ == '__main__':
    print checkMaximumElement(inp, x)
