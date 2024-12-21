stones = open('input11.txt').readline().split()

def split_stone(stone):
    l = int(len(stone)/2)
    return [str(int(stone[:l])), str(int(stone[l:]))]

# blink returns list of new stone order after a single blink
def blink(stones):
    ans = []

    # if 0, change to 1
    # if len even, split into two nums
    # else * by 2024

    for stone in stones:
        if stone == '0':
            ans.append('1')
        elif len(stone) % 2 == 0:
            ans += split_stone(stone)
        else:
            ans.append(str(int(stone)*2024))

    return ans 


for i in range(25):
    print(i)
    stones = blink(stones)

print(len(stones))

# part 2 
stones = ['890']
for i in range(75):
    print(i)
    stones = blink(stones)

print(len(stones))