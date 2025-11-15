#!/usr/bin/python3
# Yalnız bir dövrə və bir print funksiyası istifadə edərək əlifbanı çap edir.

# Bütün hərfləri saxlamaq üçün boş sətir (string)
# Bu, hərflərin dəyişəndə saxlanılması demək deyil, yalnız son çıxışı hazırlayır.
alphabet = ""

# 'a' hərfinin ASCII dəyərindən ('z' hərfinin ASCII dəyərinə qədər) dövr edirik.
# ord('a') = 97, ord('z') = 122
for i in range(ord('a'), ord('z') + 1):
    # Rəqəmi simvola çevirib sətirə əlavə edirik
    alphabet += chr(i)

# Bütün əlifbanı yeni sətir olmadan çap edirik
print("{}".format(alphabet), end="")
