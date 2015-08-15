# URL : https://www.hackerrank.com/contests/countercode/challenges/imba/submissions/code/3534534

from copy import deepcopy

def permutationsUtil(inp, fixedPart, permute, index):
    if len(fixedPart) == len(inp):
        yield fixedPart
    for i in xrange(len(permute)):
        cFixedPart = deepcopy(fixedPart)
        cPermute = deepcopy(permute)
        cFixedPart.append(permute[i])
        del cPermute[i]
        for j in permutationsUtil(inp, cFixedPart, cPermute, index + 1):
            yield j
        
        
    

def permutations(inp):
    for i in permutationsUtil(inp, [], inp, 0):
        yield i

def satisfy(i, N):
    for j in xrange(len(i) - 1):
        if abs(i[j] + i[j + 1]) <= N + 1:
            pass
        else:
            return False
    return True


# Method 1
for _ in xrange(1):
    N = 9
    a = permutations(range(1, N + 1))
    for i in a:
        if satisfy(i, N):
            print i
            break

# Method 2        
for _ in xrange(input()):
    li = [0] * N
    desc = True
    j = N
    m = 1
    for i in xrange(N - 1, -1, -1):
        if desc:
            li[i] = j
            j = j - 1
        else:
            li[i] = m
            m += 1
        desc = not desc
    print li
        

            
        

        
    
    
    