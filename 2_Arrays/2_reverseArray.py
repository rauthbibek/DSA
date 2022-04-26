def revArray(A):
    start = 0
    end = len(A)-1
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    return A

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5]
    print(revArray(A))
