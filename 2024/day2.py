f = open('2024/input2.txt')
lines = f.readlines()
reports = [[int(x) for x in line.split()] for line in lines]

# for a line to be valid
# all numbers have to be either all increasing or decreasing
# all consecutive numbers but change by 1 < change < 3

def is_valid_report(report) -> bool:
    if len(report) <= 1:
        return True

    if report[0] < report[1]: # increasing case
        for i in range(len(report)-1):
            if report[i] > report[i+1] or report[i+1] - report[i] == 0 or report[i+1] - report[i] > 3:
                return False
            
    else: # decreasing case
        for i in range(len(report)-1):
            if report[i] < report[i+1] or report[i] - report[i+1] == 0 or report[i] - report[i+1] > 3:
                return False
    
    return True
            
ans = 0
for report in reports:
    if is_valid_report(report):
        ans += 1

print(ans)

# part 2

# reports are safe if the removal of a level makes report safe

for report in reports:
    if not is_valid_report(report):
        for i in range(len(report)):
            if is_valid_report(report[:i] + report[i+1:]):
                ans += 1
                break

print(ans)
    
        
