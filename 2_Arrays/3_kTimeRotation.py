# Given an integer array "A" and an integer "k",
# you have to print the same array after rotating it "k" times towards the right.
# Example:

# A = [1, 2, 3, 4, 5, 6,7] K=3
# [1, 2, 3, 4, 5, 6, 7] ⇒ [7, 1, 2, 3, 4, 5, 6] ⇒ [6, 7, 1, 2, 3, 4, 5] ⇒ [5, 6, 7, 1, 2, 3, 4]

def reverseList(A, start, end):
    
    while start < end:
        A[start], A[end-1] = A[end-1], A[start]
        start += 1
        end -= 1
    return A

def k_time_rotation(A, k):
    N =  len(A)
    k = k % N

    # reverse the list
    A = reverseList(A, 0, N)
    # reverse 0-->k-1 index
    A = reverseList(A,0, k)
    # reverse k-->N-1 index
    A = reverseList(A, k, N)
 
    return A

if __name__ == '__main__':
    A = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(f"After {3} time rotation: {k_time_rotation(A, k)}")