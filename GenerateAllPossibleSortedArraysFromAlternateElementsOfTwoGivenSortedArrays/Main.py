# URL : http://www.geeksforgeeks.org/generate-all-possible-sorted-arrays-from-alternate-elements-of-two-given-arrays/
from copy import deepcopy
def generatePossibleSortedArraysUtilB(a, b, ai, aj, bi, bj, element):
    for i in xrange(bi, bj + 1):
        if b[i] >= element:
            return range(i, bj + 1)
    return -1

def generatePossibleSortedArraysUtilA(a, b, ai, aj, bi, bj, element, o, output):
    for i in xrange(ai, aj + 1):
        if a[i] >= element:
            out = generatePossibleSortedArraysUtilB(a, b, i, aj, bi, bj, a[i])
            if out != -1:
                for j in out:
                    co = deepcopy(o)
                    # print (a[i],b[j])
                    co.append(a[i])
                    co.append(b[j])
                    print co
                    output.append(co)
                    generatePossibleSortedArraysUtilA(a, b, i + 1, aj, j + 1, bj, b[j], co, output)
        


def generatePossibleSortedArrays(a, b):
    out = []
    generatePossibleSortedArraysUtilA(a, b, 0, len(a) - 1, 0, len(b) - 1, float('-inf'), [], out)
    return out




if __name__ == '__main__':
    a = [10, 15, 25 , 35  , 80 , 90 ]
    b = [5, 20, 30 , 40 , 60 , 70]
    out =  generatePossibleSortedArrays(a, b)
    print out
    print len(out)
