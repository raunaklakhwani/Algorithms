

count = 0
def generateCom(lists,r):
    '''
    This method takes the input list and generates all the combinations. Does not handle duplicates
    '''
    if r > len(lists):
        return
    else:
        generateComUtil(lists,r,[],0)
        
def generateComUtil(lists,r,gen,index):
    global count
    #print lists,r,gen,index,len(lists) - r + 1
    if len(gen) == r:
        count = count + 1
        print gen
    else:
        for i in xrange(index,len(lists) - r + len(gen) + 1):
            x = gen[:]
            x.append(lists[i])
            generateComUtil(lists,r,x,i+1)
        


if __name__ == '__main__':
    generateCom([1,2,3,4,5], 5)
    print count