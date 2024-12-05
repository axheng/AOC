f = open('input4.txt')
lines = f.readlines()
lines = [list(x) for x in lines]

l = len(lines)

def xmas(x,y):

    if lines[x][y] != 'X':
        return 0
    
    ans = 0
    #up
    if x-3 >= 0 and lines[x-1][y] == 'M' and lines[x-2][y] == 'A' and lines[x-3][y] == 'S':
        ans += 1
    #down 
    if x+3 < l and lines[x+1][y] == 'M' and lines[x+2][y] == 'A' and lines[x+3][y] == 'S':
        ans += 1
    #left
    if y-3 >= 0 and lines[x][y-1] == 'M' and lines[x][y-2] == 'A' and lines[x][y-3] == 'S':
        ans += 1
    #right
    if y+3 < len(lines[x]) and lines[x][y+1] == 'M' and lines[x][y+2] == 'A' and lines[x][y+3] == 'S':
        ans += 1

    # DIAGONALS 
    #ul
    if x-3 >= 0 and y-3 >= 0 and lines[x-1][y-1] == 'M' and lines[x-2][y-2] == 'A' and lines[x-3][y-3] == 'S':
        ans += 1
    #ur
    if x-3 >= 0 and y+3 < len(lines[x]) and lines[x-1][y+1] == 'M' and lines[x-2][y+2] == 'A' and lines[x-3][y+3] == 'S':
        ans += 1
    #dl
    if x+3 < l and y-3 >= 0 and lines[x+1][y-1] == 'M' and lines[x+2][y-2] == 'A' and lines[x+3][y-3] == 'S':
        ans += 1
    #dr
    if x+3 < l and y+3 < len(lines[x]) and lines[x+1][y+1] == 'M' and lines[x+2][y+2] == 'A' and lines[x+3][y+3] == 'S':
        ans += 1

    return ans

ans = 0
for x in range(l):
    for y in range(len(lines[x])):
        ans += xmas(x,y)

print(ans)

# pt 2
def x_mas(x, y):

    if lines[x][y] != 'A':
        return 0
    
    ans = 0
    if x + 1 < l and x - 1 >= 0 and y + 1 < len(lines[x]) and y - 1 >= 0:
        # CASES
        # M_M S_S M_S S_M
        # _A_ _A_ _A_ _A_
        # S_S M_M M_S S_M
        if lines[x-1][y-1] =='M' and lines[x-1][y+1] == 'M' and lines[x+1][y-1] == 'S' and lines[x+1][y+1] == 'S':
            ans = 1
        elif lines[x-1][y-1] =='S' and lines[x-1][y+1] == 'S' and lines[x+1][y-1] == 'M' and lines[x+1][y+1] == 'M':
            ans = 1
        elif lines[x-1][y-1] =='M' and lines[x-1][y+1] == 'S' and lines[x+1][y-1] == 'M' and lines[x+1][y+1] == 'S':
            ans = 1
        elif lines[x-1][y-1] =='S' and lines[x-1][y+1] == 'M' and lines[x+1][y-1] == 'S' and lines[x+1][y+1] == 'M':
            ans = 1
    return ans

ans2 = 0
for x in range(l):
    for y in range(len(lines[x])):
        ans2 += x_mas(x,y)

print(ans2)

