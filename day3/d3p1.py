def filetoarr() -> list[str]:
    file = open(r"C:\Users\mflem\OneDrive\Desktop\other projects\adventcode\adventcode 2024\day3\file.txt", "r")
    temp = file.readlines()
    file.close()
    return temp

words = filetoarr()
curr: str = ""

for word in words:
    for i in range(len(word)-3):
        if word[i:i+3] == "mul": pass