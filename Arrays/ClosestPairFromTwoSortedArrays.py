# URL : http://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/
inp = [1, 4, 5, 7]
inp1 = [10, 20, 30, 40]

i = 0
j = len(inp1) - 1
x = 50
positive = float("inf")
negative = float("-inf")

pi, pj = -1, -1
ni, nj = -1, -1
while i < len(inp) and j >= 0:
    pair = inp[i] + inp1[j]
    if pair > x:
        if positive > pair:
            positive = pair
            pi, pj = i, j
        
        j -= 1
        
    else:
        if negative < pair:
            negative = pair
            ni, nj = i, j
            
        i += 1
    
    
    
            
if positive - x < x - negative:
    print positive, pi, pj
else:
    print negative, ni, nj
            
