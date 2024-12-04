import re
f = open('input3.txt')
input = f.read()

# 1 regex and find all matches
# 2 parse all matches and get numbers
# 3 mutiply and add all matches

regex = r"mul\(\d{1,3},\d{1,3}\)"
muls = re.findall(regex, input)

muls = list(map(lambda m: [int(x) for x in m[4:-1].split(',')], muls))

ans = 0
for m in muls:
    ans += m[0] * m[1]

print(ans)

# part 2

# update and rescan w regex for do and dont
# loop thru with a "toggle" to see if its summed 

regex = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"
matches = re.findall(regex, input)

enabled = True
ans2 = 0
for match in matches:
    if match == 'do()':
        enabled = True
    elif match == 'don\'t()':
        enabled = False
    elif enabled:
        x, y = match[4:-1].split(',')
        ans2 += int(x) * int(y)

print(ans2)