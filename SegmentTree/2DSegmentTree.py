from math import ceil, log

inp = [[9, 18, 7, 13], [14, 3, 2, 10], [1, 8, 4, 9]]
seg = [0] * ((4 ** (int(ceil(log(len(inp) * len(inp[0]), 4)) + 1))) - 1)


def buildSegmentTree(seg, index, a, b, c, d, inp):
    print (a, b, c, d)
    if a == c and b == d:
        seg[index] = inp[a][b]
    elif a > c or b > d:
        return
    else:
        mid1 = (a + c) / 2
        mid2 = (b + d) / 2
        buildSegmentTree(seg, 4 * index + 1, a, b, mid1, mid2, inp)
        buildSegmentTree(seg, 4 * index + 2, a, mid2 + 1, mid1, d, inp)
        buildSegmentTree(seg, 4 * index + 3, mid1 + 1, b, c, mid2, inp)
        buildSegmentTree(seg, 4 * index + 4, mid1 + 1, mid2 + 1, c, d, inp)
        
        
        seg[index] += (seg[4 * index + 1] + seg[4 * index + 2] + seg[4 * index + 3] + seg[4 * index + 4])
        
buildSegmentTree(seg, 0, 0, 0, len(inp) - 1, len(inp[0]) - 1, inp)
        

print seg
