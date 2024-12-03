def filetoarr() -> list[str]:
    file = open(r"C:\Users\mflem\OneDrive\Desktop\other projects\adventcode\adventcode 2024\day3\file.txt", "r")
    temp = file.readlines()
    file.close()
    return temp

words = filetoarr()

