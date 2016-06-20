import heapq


class Node:
    def __init__(self, index, distance, score, visited):
        self.index = index
        self.distance = distance
        self.score = score
        self.visited = visited

    def __lt__(self, other):
        if self.visited != other.visited:
            return other.visited
        if self.distance != other.distance:
            return self.distance < other.distance
        return self.score > other.score

    def __str__(self):
        return str((self.index, self.distance, self.score, self.visited))

    def __repr__(self):
        return str(self)


n, m, start, end = map(int, input().split())
score = list(map(int, input().split()))
edges = [[0] * n for i in range(n)]

for i in range(m):
    s, t, w = map(int, input().split())
    edges[s][t] = w
    edges[t][s] = w


dis = [Node(i, 100000, 0, False) for i in range(n)]
dis[start] = Node(start, 0, score[start], True)
last = dis[start]
while last.index != end:
    for i, n in enumerate(dis):
        if n.visited:
            continue

        w = edges[n.index][last.index]
        if w == 0:
            continue

        new_node = Node(n.index,
                        last.distance + w,
                        last.score + score[n.index],
                        False)
        if new_node < n:
            dis[i] = new_node

    heapq.heapify(dis)
    last = dis[0]
    last.visited = True

print('%d %d' % (last.distance, last.score))
