from math import log, ceil
def getSegmentTreeUtil(li, low, high, tree, index):
    if low > high:
        return 
    if low == high:
        tree[index] = (li[low], 1)
    else:
        mid = low + (high - low) / 2
        getSegmentTreeUtil(li, low, mid, tree, 2 * index + 1)
        getSegmentTreeUtil(li, mid + 1, high, tree, 2 * index + 2)
        lMax, lTimes = tree[2 * index + 1]
        rMax, rTimes = tree[2 * index + 2]
        if lMax > rMax:
            tree[index] = (lMax, lTimes)
        elif lMax < rMax:
            tree[index] = (rMax, rTimes)
        else:
            tree[index] = (lMax, lTimes + rTimes)
        

def getSegmentTree(li):
    if len(li):
        tree = [(None, None)] * int(((2 ** (ceil(log(len(li), 2)) + 1)) - 1))
        getSegmentTreeUtil(li, 0, len(li) - 1, tree, 0)
        return tree

def getMaximumUtil(tree, l, r, index, low, high):
    if l == low and r == high:
        return tree[index]
    elif l > high or r < low:
        return (float("-inf"), 0)
    else:
        mid = low + (high - low) / 2
        lMax, lTimes = getMaximumUtil(tree, l, mid if r > mid else r, 2 * index + 1, low, mid)
        rMax, rTimes = getMaximumUtil(tree, (mid + 1) if l < (mid + 1) else l, r, 2 * index + 2, mid + 1, high)
        if lMax > rMax:
            return (lMax, lTimes)
        elif lMax < rMax:
            return (rMax, rTimes)
        else:
            return (lMax, lTimes + rTimes)
    
def getMaximum(tree, l, r, li):
    if tree:
        return getMaximumUtil(tree, l, r, 0, 0, len(li) - 1)

if __name__ == '__main__':
    N, M = 5, 3
    l, h = 1, 4
    s = "91093 50273 23254 15802 40081 1718 93748 15088 78507 93567 78507 91093 16342 99125 6747 77939 49105 28387 74023 64611 11380 1718 64296 25858 35108 35108 77939 68772 32663 51113 67013 93748 64611 77939 5054 64611 50273 82046 20672 40081 16342 15172 6747 94604 16342 82046 63160 12645 15088 51113 99663 16342 11380 68772 49105 20745 1752 45894 1718 28589 1718 24654 12528 35108 20741 26968 91093 64611 95874 16802 5054 67013 64611 99663 91093 89790 12528 61681 12528 16342 57307 20741 20745 13254 99125 15802 22857 57307 20741 93567 35108 11893 40081 12645 15172 24654 61681 64296 16342 45894"
    li = map(int,s.split())
    # li = map(int, raw_input().split())
    tree = getSegmentTree(li)
    print getMaximum(tree, 54, 59, li)
    print tree
    
