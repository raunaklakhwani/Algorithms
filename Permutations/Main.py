from copy import deepcopy

out = []
def permutationsUtil(inp,fixedPart,permute,index):
    if len(fixedPart) == len(inp):
        out.append(fixedPart)
    for i in xrange(len(permute)):
        cFixedPart = deepcopy(fixedPart)
        cPermute = deepcopy(permute)
        cFixedPart.append(permute[i])
        del cPermute[i]
        permutationsUtil(inp, cFixedPart, cPermute, index + 1)
        
        
    

def permutations(inp):
    permutationsUtil(inp,[],inp,0)

if __name__ == '__main__':
    s = [1,2,3]
    permutations(s)
    print out
    