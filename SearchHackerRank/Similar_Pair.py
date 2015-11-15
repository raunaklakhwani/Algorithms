#!/usr/bin/python

import sys

sys.setrecursionlimit(10000)

class Bit:
    def __init__(self, n):
        self.array = [0] * (n+1)
        self.size = n

    def add(self, idx, val = 1):
        while idx <= self.size:
            self.array[idx] += val
            idx += idx & -idx

    def get(self, idx):
        ret = 0
        while idx > 0:
            ret += self.array[idx]
            idx -= idx & -idx
        return ret

'''
def dfs(now, parent, bit):
    ret = bit.get(min(now+t, n)) - bit.get(now-t-1)
    #print now, ret
    bit.add(now)
    for x in tree[now]:
        if x != parent:
            ret += dfs(x, now, bit)
    bit.add(now, -1)
    return ret
'''

def dfs(now, parent, bit):
    ret = 0
    stack = [now]
    bit.add(now)
    next = [0] * (n+1)
    while len(stack) > 0:
        now = stack[-1]
        idx = next[now]
        if idx < len(tree[now]):
            child = tree[now][idx]
            #print 'stack push', child
            ret += bit.get(min(child+t, n)) - bit.get(child-t-1)
            stack.append(child)
            bit.add(child)
            next[now] += 1
        else:
            #print 'stack pop', now
            stack.pop()
            bit.add(now, -1)
    return ret

n, t = map(int, raw_input().strip().split())
tree = [[] for x in xrange(n+1)]
isroot = [True] * (n+1)
for x in xrange(n-1):
    a, b = map(int, raw_input().strip().split())
    tree[a].append(b)
    isroot[b] = False

for x in xrange(1, n+1):
    if isroot[x]: # root
        print dfs(x, -1, Bit(n))
        break