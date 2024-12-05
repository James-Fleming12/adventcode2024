from functools import lru_cache


def filetoarr() -> list[str]:
    file = open(r"C:\Users\mflem\OneDrive\Desktop\other projects\adventcode\adventcode 2024\day4\file.txt", "r")
    temp = file.readlines()
    file.close()
    return temp

words = filetoarr()
checks = "XMAS"

def starout(x: int, y: int, chx: int, chy: int) -> int:
    x += chx
    y += chy
    for i in range(3):
        if x < 0 or x >= len(words) or y < 0 or y >= len(words[x]): return 0
        if words[x][y] != checks[i+1]: return 0
        x+=chx
        y+=chy
    return 1

def star(x: int, y:int): # horribly slow
    response: int = 0
    response += starout(x, y, 1, 1)
    response += starout(x, y, 0, 1)
    response += starout(x, y, -1, 1)
    response += starout(x, y, 1, 0)
    response += starout(x, y, 0, 0)
    response += starout(x, y, -1, 0)
    response += starout(x, y, 1, -1)
    response += starout(x, y, 0, -1)
    response += starout(x, y, -1, -1)
    return response

res: int = 0

for i1, word in enumerate(words):
    for i2, i in enumerate(word):
        if i == " ": 
            continue
        if i == "X":
            res += star(i1, i2)

print(res)