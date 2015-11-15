# URL : http://www.geeksforgeeks.org/find-index-0-replaced-1-get-longest-continuous-sequence-1s-binary-array/
inp = [1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1]

leftIndex = -1
rightIndex = 0
maximum = float("-inf")
zeroFound = False
zeroIndex = -1
while rightIndex < len(inp):
    if inp[rightIndex] == 1:
        rightIndex += 1
    elif inp[rightIndex] == 0:
        if not zeroFound:
            zeroIndex = rightIndex
            zeroFound = True
            rightIndex += 1
        else:
            if maximum < (rightIndex - leftIndex - 1):
                maximum = (rightIndex - leftIndex - 1)
                #print leftIndex,rightIndex
            #print leftIndex,rightIndex,zeroIndex
            leftIndex = zeroIndex
            zeroIndex = rightIndex
            rightIndex += 1

if maximum < (rightIndex - leftIndex - 1):
    maximum = (rightIndex - leftIndex - 1)
            
print maximum
    
        
