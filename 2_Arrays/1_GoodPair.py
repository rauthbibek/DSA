# Given an array A and an integer B. A pair(i, j) in the array is a good pair if i != j and (A[i] + A[j] == B). Check if any good pair exist or not.
def is_goodpair(A, B):
    N = len(A)
    for i in range(N):
        for j in range(i+1, N):
            if A[i] + A[j] == B:
                return True
    return False


# driver code
if __name__ == '__main__':
    A = [1,2,3,4]
    B = 7
    if is_goodpair(A, B):
        print("Exist")
    else:
        print("Not exist")
    