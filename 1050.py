n = int(input())

total = 0
tmin = 0
tmax = 0
gmin = 0
gmax = 0

for i in range(n):
    m = int(input())
    total += m
    tmax = m if tmax < 0 else tmax + m
    tmin = m if tmin > 0 else tmin + m
    gmax = max(gmax, tmax)
    gmin = min(gmin, tmin)

print(max(gmax, total - gmin))
