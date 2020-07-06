n = int(input())
d = {'AC':0, "WA":0, "TLE":0, "RE":0}
for i in range(n):
    d[input()] += 1
for i in ['AC', "WA", "TLE", "RE"]:
    print(f'{i} x {d[i]}')