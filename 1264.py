def cross(x1, y1, x2, y2):
    return x1 * y2 - x2 * y1

T = int(input())
for i in range(T):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    d1 = cross(x3 - x1, y3 - y1, x4 - x1, y4 - y1)
    d2 = cross(x3 - x2, y3 - y2, x4 - x2, y4 - y2)
    d3 = cross(x1 - x3, y1 - y3, x2 - x3, y2 - y3)
    d4 = cross(x1 - x4, y1 - y4, x2 - x4, y2 - y4)
    print('Yes' if d1 * d2 <= 0 and d3 * d4 <= 0 else 'No')