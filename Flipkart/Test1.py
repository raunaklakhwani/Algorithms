# http://www.geeksforgeeks.org/flipkart-interview-experience-set-35-on-campus-for-sde-1/

s = list("flipkart")
v = []
for i in xrange(len(s)):
    if s[i] in "aeiou":
        v.append(i)

#v = [1,4,6]

temp = s[v[0]]
for i in xrange(1,len(v)):
    temp,s[v[i]] = s[v[i]],temp

s[v[0]] = temp
print list("flipkart")
print s

