# Remove space with %20

#s = "Ronak is a good boy"
s = "Ronak is a good boy"
i = len(s) - 1
spaces = 4

s = list(s + spaces * "  ")

h = len(s) - 1


while i >= 0:
    if s[i] == " ":
        for j in "02%":
            s[h] = j
            h -= 1
    else:
        s[h] = s[i]
        h -= 1
    i -= 1
    
print "".join(s)