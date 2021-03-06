num_of_disks = 2


def towerOfHanoiRecursive(num, source, aux, destination):
    if num > 0:
        towerOfHanoiRecursive(num - 1, source, destination, aux)
        print source , " --> ", destination
        towerOfHanoiRecursive(num - 1, aux, source, destination)
        

def towerOfHanoiIterative(num, source, aux, destination):
    '''
    URL : http://www.geeksforgeeks.org/iterative-tower-of-hanoi/
    
    1. Calculate total number of moves : i.e 2^n - 1
    2. if number of disk is even then swap destination and aux
    3. for i in 1.. total moves
    3.1 if i%3  == 1 then
        legal move between source and destination
        else if i%3 == 2 then
        legal move between source and aux
        else
        legal move between aux and destination
        
    '''
    source = (source, range(1, num + 1))
    aux = (aux, [])
    destination = (destination, [])
    totalMoves = 2 ** num - 1
    
    if num % 2 == 0:
        aux, destination = destination, aux
        
    for i in xrange(1, totalMoves + 1):
        if i % 3 == 1:
            legalMove(source, destination)
        elif i % 3 == 2:
            legalMove(source, aux)
        else:
            legalMove(destination, aux)
            
            

def legalMove(source, target):
    try :
        sourceTop = source[1][0]
    except IndexError:
        sourceTop = float("inf")
    try :
        targetTop = target[1][0]
    except IndexError:
        targetTop = float("inf")
        
    if sourceTop < targetTop:
        print source[0] , " --> ", target[0]
        target[1].insert(0, sourceTop)
        del source[1][0]
    else :
        print target[0] , " --> ", source[0]
        source[1].insert(0, targetTop)
        del target[1][0]
        


if __name__ == '__main__':
    towerOfHanoiRecursive(num_of_disks, "S", "A", "D")
    print "###################"
    towerOfHanoiIterative(num_of_disks, "S", "A", "D")
