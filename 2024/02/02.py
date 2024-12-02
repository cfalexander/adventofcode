# Part I
with open("input.txt", "r") as file:
    reps = [list(map(int, line.rstrip().split())) for line in file.readlines()]
safeCount = 0
for report in reps:
    safe = True
    for level in range(len(report) - 1):
        diff = abs(report[level] - report[level + 1])
        if diff > 3 or diff == 0:
            safe = False
    if report != sorted(report) and report != sorted(report, reverse=True):
        safe = False
    if safe:
        safeCount += 1
print("Number of safe counts: " + str(safeCount))

# Part II
safeCount = 0
def safeCheck(report):
    safe = True
    for level in range(len(report) - 1):
        diff = abs(report[level] - report[level + 1])
        if diff > 3 or diff == 0:
            safe = False
    if report != sorted(report) and report != sorted(report, reverse=True):
        safe = False
    return safe

for line in reps:
    if safeCheck(line):
        safeCount += 1
    else:
        dampener = False
        for i in range(len(line)):
            if safeCheck(line[:i] + line[i+1:]):
                dampener = True
        if dampener:
            safeCount += 1
print("Number of safe counts with dampener: " + str(safeCount))
