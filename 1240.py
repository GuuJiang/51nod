from math import sqrt

def miu(n):
    result = 1
    for d in range(2, int(sqrt(n)) + 1):
        devided = False
        while n % d == 0:
            if devided:
                return 0
            devided = True
            n /= d
        if devided:
            result = -result
        if n == 1:
            return result
    return -result

print(miu(int(input())))