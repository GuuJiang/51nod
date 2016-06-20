import math
import itertools


def rel(p0, p1, r):
    x0, y0 = p0
    x1, y1 = p1
    return 0 if (x1 - x0) ** 2 + (y1 - y0) ** 2 < r ** 2 else 1


def dis_p2p(p1, p2):
    return math.sqrt(dis_p2p2(p1, p2))


def dis_p2p2(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2


def dis_p2s(p0, p1, p2):
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    dot = (x2 - x1) * (x0 - x1) + (y2 - y1) * (y0 - y1)
    if dot <= 0:
        return dis_p2p(p0, p1)
    d = dis_p2p2(p1, p2)
    if dot >= d:
        return dis_p2p(p0, p2)
    o = dot / d
    return dis_p2p(p0, ((x1 + (x2 - x1) * o), (y1 + (y2 - y1) * o)))


def solve():
    x0, y0, r = map(int, input().split())
    p0 = (x0, y0)
    points = [tuple(map(int, input().split())) for i in range(3)]

    c = sum(rel(p0, p, r) for p in points)
    if c == 0:
        return 'No'
    if c < 3:
        return 'Yes'
    if any(dis_p2s(p0, p1, p2) <= r for p1, p2 in itertools.combinations(points, 2)):
        return 'Yes'
    else:
        return 'No'


T = int(input())
for i in range(T):
    print(solve())
