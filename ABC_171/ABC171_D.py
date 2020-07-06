import collections

n = int(input())
a = list(map(int,input().split()))
q = int(input())
b,c = [0]*q, [0]*q
for i in range(q):
    b[i],c[i] = map(int,input().split())
counter = collections.Counter(a)

s = sum(a)
for i in range(q):
    s += (c[i]-b[i])*counter[b[i]]
    print(s)
    counter[c[i]] = counter[c[i]] + counter[b[i]]
    counter[b[i]] = 0
