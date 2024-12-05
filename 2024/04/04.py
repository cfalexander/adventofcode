with open("input.txt", "r") as file:
    search = [line.rstrip() for line in file]
# Part I

def searcher(inparray):
    count = 0
    for a in range(len(inparray)):
        for b in range(len(inparray[0])):
            if inparray[a][b] == "X":
                if b > 2:
                    # backwards
                    if ''.join([inparray[a][b-i] for i in range(4)]) == "XMAS":
                        count += 1
                    # up-left
                    if a > 2:
                        if ''.join([inparray[a-i][b-i] for i in range(4)]) == "XMAS":
                            count += 1
                    # down-left
                    if a < len(inparray) - 3:
                        if ''.join([inparray[a+i][b-i] for i in range(4)]) == "XMAS":
                            count += 1
                if b < len(inparray[0]) - 3:
                    # forwards
                    if ''.join([inparray[a][b+i] for i in range(4)]) == "XMAS":
                        count += 1
                    # up-right
                    if a > 2:
                        if ''.join([inparray[a-i][b+i] for i in range(4)]) == "XMAS":
                            count += 1
                    # down-right
                    if a < len(inparray) - 3:
                        if ''.join([inparray[a+i][b+i] for i in range(4)]) == "XMAS":
                            count += 1
                if a < len(inparray) - 3:
                    # down
                    if ''.join([inparray[a+i][b] for i in range(4)]) == "XMAS":
                        count += 1
                if a > 2:
                    # up
                    if ''.join([inparray[a-i][b] for i in range(4)]) == "XMAS":
                        count += 1
    return count
print("XMAS appears", searcher(search), "times!")
# XMAS appears 2397 times!

# Part II
def cross(inparray):
    count = 0
    for a in range(1, len(inparray) - 1):
        for b in range(1, len(inparray[0]) - 1):
            if inparray[a][b] == "A":
                if set([inparray[a-1][b-1], inparray[a+1][b+1]]) == set(["M", "S"]) and set([inparray[a-1][b+1], inparray[a+1][b-1]]) == set(["M", "S"]):
                    count += 1
    return count

print("An X-MAS appears", cross(search), "times!")
# An X-MAS appears 1824 times!
