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

running: list[int] = []
failed: bool = False

for c in range(step+1, len(words)): # each line
    temp = words[c].split(",")
    temp = [int(i.strip()) for i in temp]
    running = [] # reset values
    failed = False
    for i in temp: # each number
        for j in running: # running count check
            if j in vals and i in vals[j]:
                failed = True
                break
        if failed:
            break
        running.append(i)
    if not failed:
        res += temp[len(temp)//2]

print(res)