def getMinimumHackosToPay(N, M):
    if N == 0 and M <= 0:
        return -1
    elif N == 0:
        return -1
    elif M <= N:
        return 1
    else:
        a = getMinimumHackosToPay(N - 1, M - N)
        return -1 if a == -1 else (1 + a)



if __name__ == '__main__':
    N,M = map(int,raw_input().split())    
    print getMinimumHackosToPay(N, M)