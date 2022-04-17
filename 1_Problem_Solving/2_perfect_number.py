from math import sqrt

def perfectNumber(N: int):
    sum = 1
    for i in range(2, int(sqrt(N))+1):
        if N % i == 0:
            sum += i
            if i*i != N:
                sum += N//i
    print(sum)
    if sum == N:
        print(f"{N} is a Perfect Number")
    else:
        print(f"{N} is not a Perfect Number")

if __name__ == "__main__":
    N  = int(input("Number: "))
    perfectNumber(N)