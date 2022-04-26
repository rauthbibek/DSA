# You are given an integer N you need to print all the Armstrong Numbers between 1 to N.
def is_armstrong(num):
    temp = num
    sum = 0
    while temp > 0:
        # to get a last digit
        # 153%10 --> 3
        digit = temp%10
        sum = sum + digit**3
        # to rest of the number(excluding last digit)
        # 153//10--> 15
        temp = temp//10
    if sum == num:
        # print(f"{num} is Armstrong Number")
        return True
    else:
        # print(f"{num} is not a Armstrong Number")
        return False

if __name__ == '__main__':
    # is_armstrong(133)
    N  = int(input("Number: "))
    for i in range(1,N+1):
        if is_armstrong(i):
            print(i, end=" ")

