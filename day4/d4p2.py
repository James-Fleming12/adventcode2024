def filetoarr() -> list[str]:
    file = open(r"C:\Users\mflem\OneDrive\Desktop\other projects\adventcode\adventcode 2024\day4\file.txt", "r")
    temp = file.readlines()
    file.close()
    return temp

words = filetoarr()
res: int = 0

def star(x: int, y: int) -> bool:
    mc: int = 0
    ms = [
        [-1,-1] if words[x-1][y-1] == "M" else [0,0],
        [-1,1] if words[x-1][y+1] == "M" else [0,0],
        [1,-1] if words[x+1][y-1] == "M" else [0,0],
        [1,1] if words[x+1][y+1] == "M" else [0,0],
    ]
    for i in ms:
        if i[0] != 0:
            mc += 1
    if mc != 2:
        return False
    for i in ms:
        if i[0] == 0:
            continue
        if words[x+1 if i[0] < 0 else x-1][y+1 if i[1] < 0 else y-1] != "S":
            return False
    return True

for i1 in range(1, len(words)-1): # bound checks done in loop
    for i2 in range(1, len(words[i1])-1):
        if words[i1][i2] == "A" and star(i1, i2): 
            res += 1

print(res)