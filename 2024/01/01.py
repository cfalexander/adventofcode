# Part I
with open("input.txt", 'r') as l:
    lineleft = []
    lineright = []
    for line in l:
        temp = line.rstrip().split()
        lineleft.append(temp[0])
        lineright.append(temp[1])
    lineleft.sort()
    lineright.sort()

diff = 0
for i in range(len(lineleft)):
    diff += abs(int(lineleft[i]) - int(lineright[i]))
print("The sum of differences is: " + str(diff))
# The sum of differences is: 3508942


# Part II
sscore = 0
for num in lineleft:
    if num in lineright:
        sscore += lineright.count(num) * int(num)
print("The new similarity score is: " + str(sscore))
# The new similarity score is: 26593248
