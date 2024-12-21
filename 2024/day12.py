lines = [line.strip() for line in open('input12.txt').readlines()]

regions = [] # Type: list of (str, list of (int, int))
visited = set()

# takes list of tuples and returns set of first elem in tuples
def tuple_list(tuples):
    ans = set()
    for t in tuples:
        ans.add(t[0])
    return ans

# finds all coords in the region that includes (x,y)
def subspace(x, y, char,coords):
    if 0 <= x < 140 and 0 <= y < 140 and lines[x][y] == char and (x,y) not in visited:
        visited.add((x,y))
        coords.add((x,y))
        print(char)
        subspace(x+1, y, lines[x][y], coords)
        subspace(x-1, y, lines[x][y], coords)
        subspace(x, y+1, lines[x][y], coords)
        subspace(x, y-1, lines[x][y], coords)


    
for x in range(140):
    for y in range(140):
        if lines[x][y] not in tuple_list(regions) or (x,y) not in visited: # coord not included in an existingregion
            coords = set()
            subspace(x,y, lines[x][y], coords)
            regions.append((lines[x][y], coords))


def area(region):
    return len(region[1])
    
def perim(region):
    ans = 0
    for x, y in region[1]:
        if 0 <= x-1 and lines[x-1][y] != lines[x][y]:
            ans += 1
        if 140 > x+1 and lines[x+1][y] != lines[x][y]:
            ans += 1
        if 0 <= y-1 and lines[x][y-1] != lines[x][y]:
            ans += 1
        if 140 > y+1 and lines[x][y+1] != lines[x][y]:
            ans += 1

        if x == 0 or x == 139:
            ans += 1
        if y == 0 or y == 139:
            ans += 1
    return ans

ans = 0
for region in regions:
    print(region, area(region) , perim(region))
    ans += area(region) * perim(region)

print(ans)