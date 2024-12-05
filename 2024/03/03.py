import re

# Part I
with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file]

total = 0
for line in lines:
    for n1, n2 in re.findall(r"mul\((\d+),(\d+)\)", line):
        total += int(n1)*int(n2)
print("Sum of multiplications:", total)
# Sum of multiplications: 182780583

# Part II
total2 = 0
enabled = True
for line in lines:
    for n1, n2, do, dont in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line):
        if do or dont:
            enabled = bool(do)
        else:
            total2 += int(n1)*int(n2)*enabled
print("Sum of enabled multiplications:", total2)
# Sum of enabled multiplications: 90772405

