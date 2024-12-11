lines = open('input10.txt').readlines()


grid = []

for i in range(len(lines)):
    l = []
    for j in range(len(lines[i].strip())):
        l.append(int(lines[i][j]))
    grid.append(l)

nines_visited = set()
def score(i, j):
    if 0 > i >= len(grid) or 0 > j >= len(grid[0]):
        return 0
    if grid[i][j] == 9 and (i, j) not in nines_visited:
        nines_visited.add((i, j))
        return 1
    
    ans = 0
    if (i+1) < len(grid) and grid[i+1][j] - grid[i][j] == 1:
        ans += score(i+1, j)
    if (i-1) >= 0 and grid[i-1][j] - grid[i][j] == 1:
        ans += score(i-1, j)
    if (j+1) < len(grid[0]) and grid[i][j+1] - grid[i][j] == 1:
        ans += score(i, j+1)
    if (j-1) >= 0 and grid[i][j-1] - grid[i][j] == 1:
        ans += score(i, j-1)

    return ans

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            nines_visited = set()
            ans += score(i, j)
print(ans)

# part 2 

def rate(i, j):
    if 0 > i >= len(grid) or 0 > j >= len(grid[0]):
        return 0
    if grid[i][j] == 9:
        return 1
    
    ans = 0
    if (i+1) < len(grid) and grid[i+1][j] - grid[i][j] == 1:
        ans += rate(i+1, j)
    if (i-1) >= 0 and grid[i-1][j] - grid[i][j] == 1:
        ans += rate(i-1, j)
    if (j+1) < len(grid[0]) and grid[i][j+1] - grid[i][j] == 1:
        ans += rate(i, j+1)
    if (j-1) >= 0 and grid[i][j-1] - grid[i][j] == 1:
        ans += rate(i, j-1)

    return ans

ans2 = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 0:
            ans2 += rate(i, j)
print(ans2)