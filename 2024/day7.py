lines = open('input7.txt').readlines()
lines = [line.split(': ') for line in lines]
lines = [[int(line[0]), 
          [int(x) for x in line[1].strip().split()]] 
         for line in lines]

# calculate: calculate all possibilities 
# break case: empty list
# else append first elem +/* calculate(list[1:])

def concat(i1, i2):
    return int(str(i1) + str(i2))

stuff = []
def calculate(nums, curr):
    if len(nums) == 1:
        stuff.append(curr+nums[0])
        stuff.append(curr*nums[0])
        stuff.append(concat(curr, nums[0]))
    else:
        calculate(nums[1:], curr+nums[0])
        calculate(nums[1:], curr*nums[0])
        calculate(nums[1:], concat(curr, nums[0]))
        

ans = 0
for line in lines:
    calculate(line[1], 0)
    if line[0] in stuff:
        ans += line[0]
    stuff = []
print(ans)

