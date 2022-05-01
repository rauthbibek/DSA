def maxEven_minOdd(A):
    # N = len(A)
    maxx = -999999
    minn = 999999
    for a in A:
        if a%2 == 0:
            maxx = max(maxx,a)
        else:
            minn = min(minn,a)
    
    return maxx - minn
    

if __name__ == '__main__':
    A = [1,2,3,4,5,6,7]
    print(maxEven_minOdd(A))