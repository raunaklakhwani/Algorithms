# URL : http://www.geeksforgeeks.org/merging-intervals/

def isOverlap(top, b):
    return b[0] <= top[1]
    

def getMergedIntervals(intervals):
    '''
    The idea is to sort the intervals based on starting time. Now start pushing the intervals on the stack and while pushing check 
    if its overlap then merge with top else only push
    '''
    if len(intervals):
        intervals.sort(key=lambda item:item[0])
        print intervals
        s = [intervals[0]]
        for i in xrange(1, len(intervals)):
            if isOverlap(s[-1], intervals[i]):
                s[-1] = (s[-1][0], s[-1][1] if s[-1][1] > intervals[i][1] else intervals[i][1])
            else:
                s.append(intervals[i])
        
        intervals = s
    
    return intervals

if __name__ == '__main__':
    #intervals = [(1, 9), (2, 4), (4, 7), (6, 8)]
    intervals = [(6, 8), (1, 3), (2, 4), (4, 7)]
    #intervals = [(1, 3), (7, 9), (4, 6), (10, 13)]
    print getMergedIntervals(intervals)
    
