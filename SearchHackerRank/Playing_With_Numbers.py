from bisect import bisect_left, bisect_right

N = 3
li = [-1, 2, -3]
li.sort()
Q = 3
query = [1, -2 , 3]

cumm = [0] * len(li)
cumm[0] = li[0]
for i in xrange(1, len(li)):
    cumm[i] = cumm[i - 1] + li[i]

add = 0
for q in query:
    add += q
    
    left = bisect_left(li, -1 * add)

    if left == 0:
        print cumm[-1] + N * add
    else:
        result = abs(cumm[left - 1] + left * add) + abs((cumm[-1] - cumm[left - 1] + (add * (N - left))))
        print result

