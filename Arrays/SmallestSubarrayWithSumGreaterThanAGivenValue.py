# URL : http://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/
inp = [1, 11, 100, 1, 0, 200, 3, 2, 281, 250]
x = 280

i = 0
j = 0
currSum = 0
minimum = float("inf")
while currSum <= x and  i < len(inp):
    currSum += inp[i]
    
    if currSum > x:
        while currSum - inp[j] > x:
            currSum -= inp[j]
            j += 1
        if minimum > (i - j + 1):
            minimum = i - j + 1
        currSum -= inp[j]
        j += 1
    i += 1
print minimum
    
