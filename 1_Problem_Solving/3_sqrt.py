def sqrt(N:int):
    low = 1
    high = N

    # return sqrt if N is a perfect square
    while low<=high:
        mid = (low + high) // 2
        if mid*mid > N:
            high = mid-1
        elif mid*mid < N:
            low = mid+1
        else:
            return mid
    if mid*mid == N:
        return mid
    else:
        print("It's not a perfect square")
    
if __name__ == '__main__':
    N  = int(input('Enter Number: '))
    print(sqrt(N))