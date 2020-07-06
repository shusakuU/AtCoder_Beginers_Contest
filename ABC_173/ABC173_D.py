from collections import deque
from bisect import bisect_left
n = int(input())
a = sorted(list(map(int,input().split())),reverse=True)

c = 0
q = deque([a[0]])
for i in a[1:]:
    m = q.pop()
    c += m
    q.appendleft(i)
    q.appendleft(i)
print(c)




