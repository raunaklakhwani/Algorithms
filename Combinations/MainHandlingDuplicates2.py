l = [1,2,1]
#l = [1,2,1,3,2]
#l = [1,2,3,4,5]
l = [1,2,2,4,5]

r = 4
N = len(l)


l.sort()



def recurse(res,main,index,r,l,N):
    if len(res) == r:
        main.append(res[:])
        return
    elif index == N:
        return
    
    #include
    res.append(l[index])
    recurse(res, main, index + 1, r, l, N)
    del res[-1]
    
    i = index + 1
    while i < N and l[i] == l[index]:
        i += 1
     
    #exclude
    recurse(res, main, i, r, l, N)
    
        

main = []
recurse([], main, 0, r, l, N)
print main
        
        
        
        