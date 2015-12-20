#URL : http://www.geeksforgeeks.org/prop-tiger-interview-experience/
from collections import deque
num = 893
s = deque([])
while num:
    r = num % 26
    s.appendleft(chr(64 + r))
    num = (num - r) /26
print "".join(s)