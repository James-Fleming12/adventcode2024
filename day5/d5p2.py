from functools import cmp_to_key

def filetoarr() -> list[str]:
    file = open(r"C:\Users\mflem\OneDrive\Desktop\other projects\adventcode\adventcode 2024\day5\file.txt", "r")
    temp = file.readlines()
    file.close()
    return temp

words = filetoarr()
step: int = 0
res: int = 0
vals: dict = dict()

while len(words[step]) > 1:
    temp = words[step].split("|")
    if int(temp[1]) in vals:
        vals[int(temp[1])].append(int(temp[0]))
    else:
        vals[int(temp[1])] = [int(temp[0])]
    step+=1

def custom_sort(val1, val2):
    if val2 in vals and val1 in vals[val2]:
        return -1
    if val1 in vals and val2 in vals[val1]:
        return 1
    else:
        return 0

running: list[int] = []
failed: bool = False
curr: list[int] = []

for c in range(step+1, len(words)): # each line
    temp = words[c].split(",")
    temp = [int(i.strip()) for i in temp]
    running = [] # reset values
    failed = False
    for index, i in enumerate(temp): # each number
        for index2, j in enumerate(running): # running count check
            if j in vals and i in vals[j]:
                curr = sorted(temp, key=cmp_to_key(custom_sort))
                failed = True
                break
        if failed:
            break
        running.append(i)
    if failed:
        print(curr)
        res += curr[len(curr)//2]

print(res)