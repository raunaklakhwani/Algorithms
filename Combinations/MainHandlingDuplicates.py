

count = 0
def generateCom(lists,r):
    '''
    This method takes the input list and generates all the combinations. Does handle duplicates
    '''
    lists.sort()
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
        i = index
        while i < len(lists) - r + len(gen) + 1:
            x = gen[:]
            x.append(lists[i])
            generateComUtil(lists,r,x,i+1)
            while i+1 < len(lists) and lists[i] == lists[i+1]:
                i = i + 1
            i = i + 1
            
        


if __name__ == '__main__':
    generateCom([1,2,2,4,5], 4)
    print count