def filetoarr() -> list[str]:
    file = open(r"C:\Users\mflem\OneDrive\Desktop\other projects\adventcode\adventcode 2024\day6\file.txt", "r")
    temp = file.readlines()
    file.close()
    return temp

def clean_print(arr):
    for i in arr:
        for j in i:
            print(j, end="")
        print()

words = [i.strip() for i in filetoarr()]
resA = [[j for j in i.strip()] for i in filetoarr()]
pos = [0, 0]
originalPos = [0,0]
direction = 0
locs: set = set()
res: int = 0
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

for index, word in enumerate(words):
    for index2, i in enumerate(word):
        if i == "^":
            pos = [index, index2]
            originalPos = [index, index2]

while pos[0] >= 0 and pos[0] < len(words[0]) and pos[1] >= 0 and pos[1] < len(words):
    if f"{pos[0]}:{pos[1]}:{directions[direction][0]}:{directions[direction][1]}" not in locs:
        locs.add(f"{pos[0]}:{pos[1]}:{directions[direction][0]}:{directions[direction][1]}")
    if pos[0] + directions[direction][0] >= 0 and pos[0] + directions[direction][0] < len(words[0]):
        if pos[1] + directions[direction][1] >= 0 and pos[1] + directions[direction][1] < len(words):
            if words[pos[0] + directions[direction][0]][pos[1] + directions[direction][1]] == "#":
                direction += 1
                if direction == 4: direction = 0
    pos[0] += directions[direction][0]
    pos[1] += directions[direction][1]

direction = 0
pos = originalPos

# i have absolutely no clue other than bruteforce
""" 
while pos[0] >= 0 and pos[0] < len(words[0]) and pos[1] >= 0 and pos[1] < len(words):
    if pos[0] + directions[direction][0] >= 0 and pos[0] + directions[direction][0] < len(words[0]):
        if pos[1] + directions[direction][1] >= 0 and pos[1] + directions[direction][1] < len(words):
            if words[pos[0] + directions[direction][0]][pos[1] + directions[direction][1]] == "#":
                direction += 1
                if direction == 4: direction = 0
    pos[0] += directions[direction][0]
    pos[1] += directions[direction][1]
    tempD = direction+1
    if tempD == 4:
        tempD = 0
    if f"{pos[0]+directions[tempD][0]}:{pos[1]+directions[tempD][1]}:{directions[tempD][0]}:{directions[tempD][1]}" in locs:
        print(f"{pos[0]+directions[tempD][0]}:{pos[1]+directions[tempD][1]}:{directions[tempD][0]}:{directions[tempD][1]}")
        res += 1 
"""

print(res)