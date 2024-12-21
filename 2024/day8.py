lines = [line.strip() for line in open('input8.txt').readlines()]
antennas = {}


for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] != '.':
            if lines[i][j] not in antennas.keys():
                antennas[lines[i][j]] = [(i,j)]
            else:
                antennas[lines[i][j]].append((i,j))

# for each unique antenna, go thru indicies and find distances from each other
# use this to calculate possible antinode locations
# go thru antinode locations and see if theyre within the bounds

antinodes = set()

def get_antinodes(antennas):
    for i in range(len(antennas)):
        for j in range(i+1, len(antennas)):
            x1, y1 = antennas[i]
            x2, y2 = antennas[j]
            slope = (x2-x1, y2-y1)

            antinodes.add((slope, max(x1, x2) + slope[0], y1+slope[1] if max(x1, x2) == x1 else y2+slope[1]))
            antinodes.add((slope, min(x1, x2) - slope[0], y1-slope[1] if min(x1, x2) == x1 else y2-slope[1]))

        

for antenna in antennas.keys():
    get_antinodes(antennas[antenna])

ans = set()
for s,x,y in antinodes:
    if 0 <= x < len(lines) and 0 <= y < len(lines[0]):
        ans.add((x,y))
# changed to include slope in tuple for pt 2, og ans is 313
print(len(ans))

ans2 = set()
for s, x, y in antinodes:
        curr = (x,y)
        #increase x
        while 0 <= curr[0] < len(lines) and 0 <= curr[1] < len(lines[0]):
            ans2.add(curr)
            curr = (curr[0] + s[0], curr[1] + s[1])

        curr = (x,y)
        # decrease x
        while 0 <= curr[0] < len(lines) and 0 <= curr[1] < len(lines[0]):
            ans2.add(curr)
            curr = (curr[0] - s[0], curr[1] - s[1])

for antenna in antennas.keys():
    for (x, y) in antennas[antenna]:
        ans2.add((x,y))

print(len(ans2))
        