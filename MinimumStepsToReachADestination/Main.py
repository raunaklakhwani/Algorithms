#URL : http://www.geeksforgeeks.org/minimum-steps-to-reach-a-destination/
def getMinStepsToReachADestinationUtil(start,nextStep,end):
    if abs(start) > abs(end):
        return float("inf")
    elif abs(start) == abs(end):
        return nextStep - 1
    else:
        a = getMinStepsToReachADestinationUtil(start + nextStep, nextStep + 1, end)
        b = getMinStepsToReachADestinationUtil(start - nextStep, nextStep + 1, end)
        return min(a,b)

def getMinStepsToReachADestination(N):
    result = 0
    if N != 0:
        result = getMinStepsToReachADestinationUtil(0, 1, N)
    return result


if __name__ == '__main__':
    N = 5
    print getMinStepsToReachADestination(2)