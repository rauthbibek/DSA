from math import sqrt

def primeNumber(N: int):
    # store the count of the factor
    count = 0
    # iterating upto sqrt(N), as factors
    # appearing in pair
    for i in range(1, int(sqrt(N))+1):
        if N % i == 0:
            # e.g i=6 for N=36, then the other
            # factor is also 6. Means only one one factor

            if i*i == N:
                count += 1
            count += 2
    # print(count)
    if count == 2:
        print(f"{N} is a prime number")
    else:
        print(f"{N} is not a prime number")


if __name__ == "__main__":
    N  = int(input("Press a number: "))
    primeNumber(N)