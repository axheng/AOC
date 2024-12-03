f = open('2024/input1_1.txt')
lines = f.readlines()

l1 = []
l2 = []

# pt 1
for line in lines: 
    a, b = line.split()
    l1.append(int(a))
    l2.append(int(b))

l1.sort()
l2.sort()

ans = 0
for i in range(len(l1)):
    ans += abs(l1[i] - l2[i])

print(ans)

# pt 2
ans2 = 0
for i in l1:
    freq = 0
    for j in l2:
        if i == j:
            freq += 1
    ans2 += i * freq

print(ans2)
