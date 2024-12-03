def filetoarr() -> list[str]:
    file = open(r"C:\Users\mflem\OneDrive\Desktop\other projects\adventcode\adventcode 2024\day1\file.txt", "r")
    temp = file.readlines()
    file.close()
    return temp

words = filetoarr()
l1: list[int] = []
l2: list[int] = []

for i in words:
    temp = i.split(" ")
    l1.append(int(temp[0]))
    l2.append(int(temp[-1].strip()))

l1 = sorted(l1)
l2 = sorted(l2)
res: int = 0

for index, i in enumerate(l1):
    res += abs(i-l2[index])

print(res)