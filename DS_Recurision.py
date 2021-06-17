# # # # # # # # # # # How to find recursion # # # # # # # # # #
# Step 1: Find Recursive Condition                            #
# Step 2: Find Base Condition                                 #
# Step 3: Find Unintentional Cases - Limits                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


def main():
    print("\n")
    # print(factorial(1))
    # print_fibo(10)
    # print(sumofdigits(123465))
    # print(powofnum(2, 10))
    # print(gcd(10, 4))
    # print(dectobin(11))


def dectobin(num):
    assert num == abs(int(num)), 'Positive Integers only.'
    if num == 0:
        return 0
    else:
        return num % 2 + 10 * dectobin(num//2)


def gcd(x, y):
    x, y = abs(x), abs(y)
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def powofnum(x, n):
    if n == 0:
        return 1
    else:
        return x * powofnum(x, n-1)


def sumofdigits(n):
    assert n >= 0 and int(n) == n, 'postive integers only'
    if n < 9:
        return n
    else:
        return n % 10 + sumofdigits(n//10)


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)


def print_fibo(n):
    arr = []
    for i in range(n):
        arr.append(fibo(i))
    print(arr)


def fibo(num):
    assert num >= 0 and int(
        num) == num, 'Fibonacci takes only positive integers.'
    if num <= 1:
        return num
    else:
        return fibo(num-1) + fibo(num-2)


if __name__ == '__main__':
    main()
