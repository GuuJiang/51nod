n = int(input())
last = -1
result = -1
for i in range(n):
    c = int(input())
    last = c if last < 0 else last + c
    result = max(last, result)
print(result)
