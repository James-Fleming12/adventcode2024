def filetoarr() -> list[str]:
    file = open(r"C:\Users\mflem\OneDrive\Desktop\other projects\adventcode\adventcode 2024\day2\file.txt", "r")
    temp = file.readlines()
    file.close()
    return temp

increasing = False
res: int = 0

words = filetoarr()
for i in words:
    temp = [int(item) for item in i.split(" ")]
    if temp[0] < temp[1]:
        increasing = True
    else:
        increasing = False
    safe = True
    for j in range(len(temp)-1):
        if increasing and temp[j] > temp[j+1]:
            safe = False
        if not increasing and temp[j] < temp[j+1]:
            safe = False
        if abs(temp[j+1]-temp[j]) > 3 or abs(temp[j+1]-temp[j]) < 1:
            safe = False
    if safe:
        res += 1

print(res)