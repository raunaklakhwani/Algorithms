coins = [1,5,10,25]
coins = [1,2,5,10]
#coins = [1,5]
d = {} # stores tuples of the form (# of coins, [coin list])

# finds the minimum # of coins needed to
# make change for some number of cents
def m(cents):
    if cents in d.keys():
        return d[cents]
    elif cents > 0:
        choices = [(m(cents - x)[0] + 1, m(cents - x)[1] + [x]) for x in coins if cents >= x]

        # given a list of tuples, python's min function
        # uses the first element of each tuple for comparison
        d[cents] = min(choices)
        return d[cents]
    else:
        d[0] = (0, [])
        return d[0]

for x in range(1, 21):
    val = m(x)
    print x, "cents requires", val[0], "coins:", val[1]