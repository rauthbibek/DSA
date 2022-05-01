def elements_greaterthanB(A, B):
    N  = len(A)
    maxx = B
    result = 0
    for i in range(N):
        if A[i] > B:
            result += 1
        elif A[i] == B:
            maxx = -1

    # if B is not present in the list
    if maxx != -1:
        return -1
    return result

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6]
    B = 8
    print(elements_greaterthanB(A, B))