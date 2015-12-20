#URL : http://www.geeksforgeeks.org/prop-tiger-interview-experience/
'''
Description : 
MS Excel columns has a pattern like A, B, C, … ,Z, AA, AB, AC,…. ,AZ, BA, BB, … ZZ, AAA, AAB ….. etc. 
In other words, column 1 is named as “A”, column 2 as “B”, column 27 as “AA”. 
Find Excel column name from a given column number like 705 AAC.
'''
from collections import deque
num = 893
s = deque([])
while num:
    r = num % 26
    s.appendleft(chr(64 + r))
    num = (num - r) /26
print "".join(s)