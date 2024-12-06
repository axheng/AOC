f = open('input5.txt')
lines = f.readlines()
rules = lines[:1176]
updates = lines[1177:]

x = []
y = []
for r in rules:
    a, b = r.split("|")
    x.append(int(a))
    y.append(int(b))

temp = []
for upd in updates:
    ints = []
    for n in upd.split(','):
        ints.append(int(n))
    temp.append(ints)
updates = temp

def is_valid(upd):
    visited = []
    ans = True

    # X|Y: if X,Y in upd then X MUST show up before Y

    for elem in upd:
        s_idx = [i for i in range(len(y)) if y[i]==elem]
        for i in s_idx:
            if x[i] in upd and y[i] in upd and x[i] not in visited:
                ans = False
            
        visited.append(elem)
    
    return ans

valid = []
invalid = []
for upd in updates:
    
    if is_valid(upd):
         valid.append(upd)
    else: invalid.append(upd)

ans = 0
for upd in valid:
    ans += upd[int(len(upd)/2)]
print(ans)
    
# part 2 

# rebuild updates inserting ints in a new index until its valid lol

rebuilt = []
for upd in invalid:
    
    new_upd = [] 
    while len(upd) != 0:
        curr = upd.pop(0)
        if(is_valid(new_upd+[curr])):
            new_upd.append(curr)
        else:
            i = 0
            while not is_valid(new_upd[:i] + [curr] + new_upd[i:]):
                i += 1
            new_upd = new_upd[:i] + [curr] + new_upd[i:]
    rebuilt.append(new_upd)

ans2 = 0
for upd in rebuilt:
    ans2 += upd[int(len(upd)/2)]
print(ans2)



