#!/usr/bin/python3
# Əlifbanı çap etmək üçün bir dövrə və bir print istifadə olunur.
alphabet = ""

# ASCII dəyərləri üzərində dövr (97='a' dan 122='z' qədər)
for i in range(ord('a'), ord('z') + 1):
    alphabet += chr(i)

# Bütün əlifbanı yeni sətir olmadan çap edirik
print("{}".format(alphabet), end="")
