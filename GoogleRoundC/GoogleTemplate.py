'''
2
2 4 1
2 1 -2 -1
3 3
-2 1
1 3 1
1 -1 -2
-2 2

1
8 8 5
7 1 6 -1 -9 4 6 5
-3 4
3 6
-6 6
-9 3
-7 3
-9 6
7 3
-6 0

1
8 8 0
7 1 6 -1 -9 4 6 5
-3 4
3 4
-6 6
-9 2
-7 2
-9 6
7 3
-6 0
'''

from math import ceil
from _collections import deque

class Node:
    def __init__(self, x, h, v, isOpp):
        self.x = x
        self.h = h
        self.v = v
        self.isOpp = isOpp
        
    def __repr__(self):
        return str(self.x) + " " + str(self.h) + " " + str(self.v) 
        

newAns = float("inf")
def calcTime(nodes,velo):
    global newAns
    #===========================================================================
    # for node in nodes:
    #     print "[",node.x,node.h,velo[node.h],"]",
    # print
    #===========================================================================
    
    t = float("-inf")
    for node in nodes:
        if node.x > 0 and velo[node.h] > 0:
            t = float("inf")
            break
        if node.x < 0 and velo[node.h] < 0:
            t = float("inf")
            break
        elif velo[node.h] == 0 and node.x!= 0:
            t = float("inf")
            break
        elif node.x == 0:
            time = 0
            t = max(t,time)
            continue
        time = int(ceil(abs(float(node.x)) / abs(velo[node.h])))
        t = max(t, time)
    else:    
        newAns = min(newAns, t)
        
        
    
        

def recurse1(nodes, oppNodes, count, index, E, H, velo):
    #===========================================================================
    # if index < len(nodes):
    #     print nodes[index]
    #===========================================================================
    if E < 0:
        return
    elif E == 0:
        calcTime(nodes,velo)
    elif index == len(nodes):
        calcTime(nodes,velo)
    else:
        node = nodes[index]
        
        if node.x > 0 and velo[node.h] > 0:
            for i in xrange(0, H):
                if velo[i] < 0:
                    diff = abs(i - node.h)
                    preH = node.h
                    node.h = i
                    recurse1(nodes, oppNodes, count, index + 1, E - diff, H, velo)
                    node.h = preH
        elif node.x < 0 and velo[node.h] < 0:
            for i in xrange(0, H):
                if velo[i] > 0:
                    diff = abs(i - node.h)
                    preH = node.h
                    node.h = i
                    recurse1(nodes, oppNodes, count, index + 1, E - diff, H, velo)
                    node.h = preH
        elif node.x > 0:
            for i in xrange(0, H):
                if velo[i] < 0:
                    diff = abs(i - node.h)
                    preH = node.h
                    node.h = i
                    recurse1(nodes, oppNodes, count, index + 1, E - diff, H, velo)
                    node.h = preH
        elif node.x < 0:
            for i in xrange(0, H):
                if velo[i] > 0:
                    diff = abs(i - node.h)
                    preH = node.h
                    node.h = i
                    recurse1(nodes, oppNodes, count, index + 1, E - diff, H, velo)
                    node.h = preH
        else:
            recurse1(nodes, oppNodes, count, index + 1, E, H, velo)
            
                        
        
                
    
    

if __name__ == '__main__':
    with open("fourth.txt", "w+") as f:
        for t in xrange(input()):
            B, H, E = map(int, raw_input().split())
            velo = map(int, raw_input().split())
            
                
            
            nodes = list([])   
            count = 0 
            oppNodes = set([])   
            for i in xrange(B):
                isOpp = False
                x, h = map(int, raw_input().split())
                
                #===============================================================
                # if x < 0 and velo[h] < 0:
                #     isOpp = True
                #     count += 1
                # elif x > 0 and velo[h] > 0:
                #     isOpp = True
                #     count += 1
                #===============================================================
                
                node = Node(x, h, velo[h], isOpp)
                # print node.x,node.h,node.v
                #===============================================================
                # if isOpp:
                #     nodes.append(node)
                #     oppNodes.add(node)
                # else:
                #     nodes.append(node)
                #===============================================================
                nodes.append(node)
                
                
            if count > E:        
                out = "Case #" + str(t + 1) + ": " + "IMPOSSIBLE" + "\n"
                print out
                f.write(out) 
                continue
            
            
            
            
            
                
            
            
            
            newAns = float("inf")
            recurse1(nodes, oppNodes, count, 0, E, H, velo)
            result = str(newAns) if newAns != float("inf") else "IMPOSSIBLE"
            # print result
            # result = getResult()
            
            out = "Case #" + str(t + 1) + ": " + result + "\n"
            print out
            f.write(out)
