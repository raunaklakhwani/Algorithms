def getFractionalBits(num):
    if num < 0 or num > 1:
        return "ERROR"
    ind = 0
    s = "0."
    while num != 0 and ind < 32:
        num = num * 2
        if num >= 1:
            num = num - 1
            s += "1"
        else:
            s += "0"
        ind += 1

    if num == 0:
        return s
    else:
        return "ERROR"
    
    
    
if __name__ == '__main__':
    print getFractionalBits(0.625)
