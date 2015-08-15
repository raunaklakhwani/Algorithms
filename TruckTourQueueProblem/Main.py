# URL : https://www.hackerrank.com/challenges/truck-tour/submissions/code/12796870

N = input()
li = []
sums = []
s = 0
ind = 0
negateFound = False
for i in xrange(N):
    petrol,distance = map(int,raw_input().split())
    s = s + petrol-distance
    sums.append(s)
    if s < 0 :
        s = 0
        negateFound = True
    else:
        if negateFound:
            ind = i
            negateFound = False
print ind
