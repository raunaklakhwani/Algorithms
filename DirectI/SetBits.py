# URL : https://www.codechef.com/DI14R018/problems/CHOBITS/
class BitArray:
    def __init__(self,size):
        self.size = size
        self.bytes = [0] * (size / (24* 8) + 1)
        
    def setBit(self,index,value):
        if index < self.size:
            ind = index / (24*8)
            ind1 = index % (24*8)
            if value:
                self.bytes[ind] = self.bytes[ind] | (1 << (191-ind1))
            else:
                self.bytes[ind] = self.bytes[ind] & (~(1 << (191-ind1)))
            
    def getBit(self,index):
        ind = index / (24*8)
        ind1 = index % (24*8)
        return (self.bytes[ind]>>(191-ind1)) & 1
    
def toggle(bit):
    return 0 if bit else 1

def processByte(h,byte,currentBit):
    key = 3
    keyData = 0
    for i in xrange(191,-1,-1):
        bit = byte>>i & 1
        if bit:
            currentBit = toggle(currentBit)
        
        if currentBit:
            keyData += 2**key
        key -= 1
        if key == -1:
            key = 3
            h[keyData] += 1
            keyData = 0
            
    

from collections import defaultdict
li = [(1,4),(9999997,10000000)]
bit = BitArray(10**7)
for a,b in li:
    bit.setBit(a-1,0 if bit.getBit(a-1) else 1)
    bit.setBit(b,0 if bit.getBit(b) else 1)

h = defaultdict(int)
currentBit = 0
for byte in bit.bytes:
    currentBit = processByte(h,byte,currentBit)
    #print h
    
print h
    
        
            
    