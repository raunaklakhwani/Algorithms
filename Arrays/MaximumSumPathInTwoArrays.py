# URL : http://www.geeksforgeeks.org/maximum-sum-path-across-two-arrays/
inp = [2, 3, 7, 10, 12, 15, 30, 34]
inp1 = [1, 5, 7, 8, 10, 15, 16, 19]

#===============================================================================
# inp = [2, 3, 7, 10, 12]
# inp1 = [1, 5, 7, 8]
# 
# inp = [10, 12]
# inp1 = [5, 7, 9]
#===============================================================================

i = 0
j = 0
fSum = sSum = 0
finalSum = 0
while i < len(inp) and j < len(inp1):
    if inp[i] < inp1[j]:
        fSum += inp[i]
        i += 1
    elif inp[i] > inp1[j]:
        sSum += inp1[j]
        j += 1
    else:
        if fSum > sSum:
            finalSum += (fSum + inp[i])
        else:
            finalSum += (sSum + inp1[j])
            
        i += 1
        j += 1
        fSum = 0
        sSum = 0


if i < len(inp):
    while i < len(inp):
        fSum += inp[i]
        i += 1
        
if j < len(inp1):
    while j < len(inp1):
        sSum += inp1[j]
        j += 1
        
if fSum != 0 or sSum != 0:
    if fSum > sSum:
        finalSum += (fSum)
    else:
        finalSum += (sSum)
        
print finalSum

        
