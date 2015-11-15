'''
abcdefghijklmnopqraastuvaaawxyzaaaa
'''
from collections import Counter

if __name__ == '__main__':
    s = raw_input()
    
    c = Counter(s)
    print c
    
    for i in xrange(97,123):
        if c[chr(i)] == 0:
            print chr(i)
            break
    else:
        j = 1
        while True:
            try:
                x = s.index("a" * j)
                j += 1
            except:
                print "a" * j
                break
                
    
        
    
    
    
    