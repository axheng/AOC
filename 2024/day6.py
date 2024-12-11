f = open('input6.txt')
lines = f.readlines()

# find guard

# traverse map:
#   if next is empty: go to spot, add idx to visited set
#   if next is obsticle: turn soldier, continue
# stop when solder out of bounds 
l = len(lines)
w = len(lines[0]) - 1

for x in range(l):
    for y in range(w):
        if lines[x][y] == '^': pos = (x, y)

dir = 'n'
og_pos = pos
visited = {pos}


    
x = pos[0]
y = pos[1]
while 0 < x < l and 0 < y < w:
    if dir == 'n':
        
        if lines[x-1][y] == '.':
            pos = (x-1, y)
            visited.add(pos)
        else: dir = 'e'
    elif dir == 'e':
        if lines[x][y+1] == '.':
            pos = (x, y+1)
            visited.add(pos)
        else: dir = 's'
    elif dir == 's':
        if lines[x+1][y] == '.':
            pos = (x+1, y)
            visited.add(pos)
        else: dir = 'w'
    elif dir == 'w':
        if lines[x][y-1] == '.':
            pos = (x, y-1)
            visited.add(pos)
        else: dir = 'n'

    x = pos[0]
    y = pos[1]

print(len(visited))

# in a loop when: visited same splot facing the same direction

loop_obs = set()
for a in range(l):
    for b in range(w):
        new_obs = (a,b)
        x = og_pos[0]
        y = og_pos[1]
        pos = og_pos
        dir = 'n'
        visited = {(pos, dir)}

        while 0 < x < l-1 and 0 < y < w-1:
            if dir == 'n':
                if (lines[x-1][y] == '.' or lines[x-1][y] == '^') and (x-1,y) != new_obs:
                    pos = (x-1, y)
                    visited.add((pos, dir))
                else: dir = 'e'
            elif dir == 'e':
                if (lines[x][y+1] == '.' or lines[x][y+1] == '^') and (x,y+1) != new_obs:
                    pos = (x, y+1)
                    visited.add((pos, dir))
                else: dir = 's'
            elif dir == 's':
                if (lines[x+1][y] == '.' or lines[x+1][y] == '^') and (x+1,y) != new_obs:
                    pos = (x+1, y)
                    visited.add((pos, dir))
                else: dir = 'w'
            elif dir == 'w':
                if (lines[x][y-1] == '.' or lines[x][y-1] == '^') and (x,y-1) != new_obs:
                    pos = (x, y-1)
                    visited.add((pos, dir))
                else: dir = 'n'
            
            x = pos[0]
            y = pos[1]

            if ((x,y), dir) in visited:
                loop_obs.add(new_obs)
                break

print(len(loop_obs))

