from operator import sub


def triple_product(x, y, z):
    return \
        x[0] * y[1] * z[2] +\
        x[1] * y[2] * z[0] +\
        x[2] * y[0] * z[1] -\
        x[0] * y[2] * z[1] -\
        x[1] * y[0] * z[2] -\
        x[2] * y[1] * z[0]

T = int(input())
for i in range(T):
    o = tuple(map(int, input().split()))
    a, b, c = (tuple(map(sub, map(int, input().split()), o)) for i in range(3))
    if triple_product(a, b, c) == 0:
        print('Yes')
    else:
        print('No')
