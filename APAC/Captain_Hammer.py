from math import asin,degrees

calAngle = lambda v,d: (9.8 * d) / (v ** 2)

def getDegreeAngle(angle):
    #print angle,
    if angle > 1:
        angle = 1
    return round((degrees(asin(angle)) / 2.0),6)

if __name__ == '__main__':
    with open("out.txt","w") as f:
        for t in xrange(input()):
            V,D = map(int,raw_input().split())
            angle = calAngle(V,D)
            #print V,D,
            result = getDegreeAngle(angle)
            
            
            out = "Case #" + str(t + 1) + ": " + str(result)
            f.write(out)
            f.write("\n")
            print out
            out
        
        
    
    