import bisect
n = int(input())
x = [0]
while x[-1] < 1000000000000001:
    x.append(x[-1]+26**(len(x)))
d = 'abcdefghijklmnopqrstuvwxyz'
digits = bisect.bisect_left(x,n)
num = n - x[digits-1]-1
ans = ""
for i in range(digits):
    ans = ''.join([d[num%(26)],ans])
    num = num//26
print(ans) 