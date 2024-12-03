def filetoarr() -> list[str]:
    file = open(r"C:\Users\mflem\OneDrive\Desktop\other projects\adventcode\adventcode 2024\day1\file.txt", "r")
    temp = file.readlines()
    file.close()
    return temp

words = filetoarr()
l2: dict = dict()

for i in words:
    temp = i.split(" ")
    t2 = int(temp[-1].strip())
    if t2 in l2:
        l2[t2] += 1
    else:
        l2[t2] = 1

res: int = 0

for i in words:
    temp = i.split(" ")
    t1 = int(temp[0])
    if t1 in l2:
        res += t1 * l2[t1]

print(res)