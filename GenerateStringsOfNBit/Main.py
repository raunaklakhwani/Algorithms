N = 5


def generateStringOfNBit(N,temp):
    if N==0:
        return ["".join(temp)]
    else:
        out = []
        temp[N - 1] = "0"
        a = generateStringOfNBit(N - 1, temp)
        temp[N - 1] = "1"
        b = generateStringOfNBit(N - 1, temp)
        out.extend(a)
        out.extend(b)
        return out
    
if __name__ == '__main__':
    print generateStringOfNBit(N,["0"] * N)