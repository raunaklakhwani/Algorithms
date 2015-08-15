from collections import deque



def reverse(q):
    if len(q) == 0:
        return
    item = q.popleft()
    reverse(q)
    q.append(item)
    
    
if __name__ == '__main__':
    q = deque([1,2,3,4,5])
    print q
    reverse(q)
    print q