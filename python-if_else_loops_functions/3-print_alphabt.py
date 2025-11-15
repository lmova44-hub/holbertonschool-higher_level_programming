#!/usr/bin/python3
# Əlifbanı çap edir, 'e' və 'q' hərfləri istisna olmaqla.
alphabet = ""

# ASCII dəyərləri üzərində dövr ('a' dan 'z' qədər)
for i in range(ord('a'), ord('z') + 1):
    current_char = chr(i)
    
    # 'e' və 'q' hərflərini yoxla və əgər yoxdursa, əlavə et
    if current_char != 'e' and current_char != 'q':
        alphabet += current_char

# Bütün əlifbanı yeni sətir olmadan çap edirik
print("{}".format(alphabet), end="")
