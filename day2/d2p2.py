# not completed (currently too low)

def filetoarr() -> list[str]:
    file = open(r"C:\Users\mflem\OneDrive\Desktop\other projects\adventcode\adventcode 2024\day2\file.txt", "r")
    temp = file.readlines()
    file.close()
    return temp

increasing = False
skip: bool = False
failed: bool = False
res: int = 0

words = filetoarr()
for i in words:
    temp = [int(item) for item in i.split(" ")]
    if temp[0] < temp[1]:
        increasing = True
    else:
        increasing = False
    safe = True
    skip = False
    failed = False
    for j in range(len(temp)-1):
        if skip:
            skip = False
            continue
        if increasing and temp[j] > temp[j+1]:
            if not failed and j+2 < len(temp) and temp[j] < temp[j+2]:
                skip = True
                failed = True
                continue
            safe = False
        if not increasing and temp[j] < temp[j+1]:
            if not failed and j+2 < len(temp) and temp[j] > temp[j+2]:
                skip = True
                failed = True
                continue
            safe = False
        if abs(temp[j+1]-temp[j]) > 3 or abs(temp[j+1]-temp[j]) < 1:
            if not failed and j+2 < len(temp) and abs(temp[j+2]-temp[j]) <= 3 and abs(temp[j+2]-temp[j]) >= 1:
                skip = True
                failed = True
                continue
            safe = False
    if safe:
        res += 1

print(res)
