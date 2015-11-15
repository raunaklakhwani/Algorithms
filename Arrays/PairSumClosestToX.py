#URL : http://geeksquiz.com/given-sorted-array-number-x-find-pair-array-whose-sum-closest-x/
inp = [1, 3, 4, 7, 10]
x = 15

positive = float("-inf")
negative = float("-inf")

start = 0
end = len(inp) - 1
while start < end:
    sum = inp[start] + inp[end]
    if sum > x:
        if sum > positive:
            positive = sum
        end = end - 1
    else:
        if sum > negative:
            negative = sum
        start = start + 1
            
if x-negative < positive - x:
    print negative
else:
    print positive

        