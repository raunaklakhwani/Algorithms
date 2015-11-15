# URL : http://www.geeksforgeeks.org/trapping-rain-water/
from _collections import deque
def getTrappedAmountWater(li):
    if len(li) > 2:
        left = []
        leftMax = li[0]
        for i, v in enumerate(li):
            if i == 0:
                left.append(v)
            else:
                left.append(leftMax)
                if v > leftMax:
                    leftMax = v
           
        print left         
        right = deque([])
        rightMax = li[-1]
        
        for i, v in reversed(list(enumerate(li))):
            if i == len(li) - 1:
                right.append(v)
            else:
                right.append(rightMax)
                if v > rightMax:
                    rightMax = v
        
        print right
        
        value = 0
        for i in xrange(1, len(li) - 1):
            minimum = min(left[i], right[i])
            if minimum > li[i]:
                value += (minimum - li[i])
        return value
    else:
        return 0
            
            
            
                
            
            
        

if __name__ == '__main__':
    li = [3, 2, 1, 4, 1, 5]
    li = [2, 0, 2]
    li = [3, 0, 0, 2, 0, 4]
    print getTrappedAmountWater(li)
    
