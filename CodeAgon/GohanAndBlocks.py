from collections import deque
s = "helloworld"
originals = s
s = deque(s)
count = 0
count1 = 0
map = {}
def getAns(stack, s, out):
    global count, count1
    if len(s) and len(stack):
        stack.append(s.popleft())
        getAns(stack, s, out)
        s.appendleft(stack.pop())
        out.append(stack.pop())
        getAns(stack, s, out)
        stack.append(out.pop())
    elif len(out) == len(originals):
        s1 = "".join(out)
        if map.get(s1) is None:
            map[s1] = 1
            count += 1
        if s1 == originals:
            count1 += 1
    elif len(s):
        stack.append(s.popleft())
        getAns(stack, s, out)
        s.appendleft(stack.pop())
        
    elif len(stack):
        out.append(stack.pop())
        getAns(stack, s, out)
        stack.append(out.pop())
        
        
getAns([], s, deque([]))
print count1,count


        
    
    
        
    
