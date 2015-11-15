#URL : http://www.geeksforgeeks.org/find-the-row-with-maximum-number-1s/
from bisect import bisect_left
li = [[0, 1, 1, 1], [0, 0, 1, 1], [0, 1, 1, 1], [0, 0, 0, 0]]

row = len(li)
col = len(li[0])

maximum = float("-inf")

r = 0
c = 0
while r < row:
    while c < col:
        element = li[r][c]
        if element == 0:
            c += 1
            if c == col:
                r += 1
                c = 0
                if r == row:
                    break
        else:
            maximum = max(maximum, row - c)
            r += 1
            if r == row or maximum == row:
                break
            if c != 0 and li[r][c - 1] == 1:
                c = bisect_left(li[r], 1, 0, c)
                
    if r == row or maximum == row:
        break
    
print maximum
    
            
            
        



    
