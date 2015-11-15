# URL : https://www.hackerrank.com/challenges/even-tree

def getEvenConnectedComponents(al, root, source, out):
    edges = al[root]
    if len(edges) == 1:
        out[root] = 1
        return 1
    else:
        s = 1
        for i in edges:
            if i != source:
                s = s + getEvenConnectedComponents(al, i, root, out)
        out[root] = s
        return s

           
def getComponents(al,root,source,out):
    edges = al[root]
    if len(edges) == 1:
        return 0
    else:
        c = 0 
        for d in al[root]:
            if d != source:
                if not (out[d] & 1):
                    c += 1
                c = c + getComponents(al, d, root, out)
        return c
                
            


N, M = map(int,raw_input().split())
#edges = [(2, 1), (3, 1), (4, 3), (5, 2), (6, 1), (7, 2), (8, 6), (9, 8), (10, 8)]
al = [[] for i in xrange(N)]
for _ in xrange(M):
    s,d = map(int,raw_input().split())
    al[s - 1].append(d - 1)
    al[d - 1].append(s - 1)

out = [0] * len(al)
getEvenConnectedComponents(al, 0, -1, out)

#print al
#print out
print getComponents(al, 0, -1, out) 
       