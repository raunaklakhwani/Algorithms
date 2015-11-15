# li = [1, 2, 3, 3, 4, 5, 2]
# li = [2, 3, 1, 3, 5, 3, 7, 8, 3]
# li = [3, 5, -3, -4, 5, -3, 7, -8, 3]
li = [3, 1, 2, 3, 6, 3]

curr = 0
maximum = float("-inf")
h = {}
activeIndex = float("-inf")
i = 0
while i < len(li):
    e = li[i]
    if h.get(e) is None:
        h[e] = i
        if e > e + curr:
            curr = e
            h = {}
            h[curr] = i
        else:
            curr = e + curr
        maximum = max(maximum, curr)
        i += 1
    else:
        i = h.get(e) + 1
        h = {}
        curr = 0
        
    
print maximum
    
